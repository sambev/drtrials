/**
 * @module trialApp
 * All the functionality to update the view and handle requests from it in
 * regards to working with Trial objects
 */
var trialApp = angular.module('trialApp', []);

trialApp.controller('TrialEditController', [
    '$scope',
    '$http',
    '$window',
    function ($scope, $http, $window) {
        var trial_id = $window.location.pathname.split('/')[2];
        var url = '/trials/' + trial_id;

        $http.get(url).then(function (resp) {
            $scope.trial = resp.data;
        });

        $scope.add_race = function () {
            if ($scope.new_race) {
                $scope.trial.races.push($scope.new_race);
                $scope.update_trial();
                $scope.new_race = null;
            }
        }

        $scope.add_rider = function () {
            if ($scope.new_rider) {
                $scope.trial.riders.push($scope.new_rider)
                $scope.update_trial();
                $scope.new_rider = null;
            }
        }

        $scope.save_trial = function () {
            var req = $http({
                url: '/trials/',
                method: 'POST',
                data: $scope.trial
            });

            req.then(function (resp) {
                $scope.trial = {
                    city: null,
                    races: []
                };
            });
        }

        $scope.update_trial = function () {
            $http.put(url, $scope.trial).then(function (resp) {
                $scope.trial = resp.data;
                $scope.selected = _.filter($scope.trial.riders, function (rider) {
                    return rider.number == $scope.selected.number;
                })[0];
            });
        }


        $scope.select_rider = function (rider) {
            $scope.selected = rider;
        }
    }
]);
