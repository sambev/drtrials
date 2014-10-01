/**
 * @module leaderApp
 * all the functionality for the leaderboard's receiving of updates
 */
var leaderApp = angular.module('leaderApp', []);

leaderApp.controller('LeaderboardController', [
    '$scope',
    function ($scope) {
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
            console.log(event);
            $scope.rider_info = JSON.parse(event.data);
            $scope.$apply()
            console.log($scope.rider_info);
        };
    }
]);
