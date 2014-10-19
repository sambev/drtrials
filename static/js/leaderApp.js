/**
 * @module leaderApp
 * all the functionality for the leaderboard's receiving of updates
 */
var leaderApp = angular.module('leaderApp', []);

leaderApp.controller('LeaderboardController', [
    '$scope',
    '$http',
    '$window',
    '$interval',
    '$timeout',
    function ($scope, $http, $window, $interval, $timeout) {
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
            $scope.trial = JSON.parse(event.data);
            $scope.$apply()
        };

        var trial_id = $window.location.pathname.split('/')[2];
        var url = '/trials/' + trial_id;

        $http.get(url).then(function (resp) {
            $scope.trial = resp.data;
        });

        var ten_shown = document.getElementsByClassName('table-wrap')[0];

        function scrollDown() {
            var max_scroll = ten_shown.scrollHeight - ten_shown.offsetHeight;
            if (ten_shown.scrollTop < max_scroll) {
                ten_shown.scrollTop = ten_shown.scrollTop + 1;
                $timeout(scrollDown, 10);
            }
        }

        function scrollUp() {
            if (ten_shown.scrollTop > 0) {
                ten_shown.scrollTop = ten_shown.scrollTop - 1;
                $timeout(scrollUp, 10);
            }
        }

        $interval(function () {
            scrollDown();
            $timeout(function () {
                scrollUp();
            }, 11000);
        }, 30000)
    }
]);
