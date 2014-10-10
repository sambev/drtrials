/**
 * @module leaderApp
 * all the functionality for the leaderboard's receiving of updates
 */
var leaderApp = angular.module('leaderApp', []);

leaderApp.controller('LeaderboardController', [
    '$scope',
    '$http',
    '$window',
    function ($scope, $http, $window) {
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
            console.log(JSON.parse(event.data));
            $scope.trial = JSON.parse(event.data);
            $scope.$apply()
        };

        var trial_id = $window.location.pathname.split('/')[2];
        var url = '/trials/' + trial_id;

        $http.get(url).then(function (resp) {
            $scope.trial = resp.data;
        });
    }
]);
