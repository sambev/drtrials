/**
 * @module leaderApp
 * all the functionality for the leaderboard's receiving of updates
 */
var leaderApp = angular.module('leaderApp', []);

leaderApp.controller('LeaderboardController', [
    '$scope',
    '$http',
    function ($scope, $http) {
        var socket = new WebSocket('ws://localhost:9000');

        socket.onopen = function (event) {
            console.log('connection success');
        };

        socket.onerror = function (event) {
            console.error('socket error: ' + event);
        };

        socket.onclose = function (event) {
            console.log('connection closed');
        };

        socket.onmessage = function (event) {
            $scope.rider_info = JSON.parse(event.data);
            $scope.$apply()
        };

        $http.get('/rider/').then(function (resp) {
            $scope.rider_info = resp.data;
        });
    }
]);
