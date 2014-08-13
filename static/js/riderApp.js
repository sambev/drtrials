/**
 * @module riderApp
 * All the functionality to update the view and handle requests from it in
 * regards to working with Rider objects
 */
var riderApp = angular.module('riderApp', []);

/**
 * @class RiderController
 * @dependency {Object} $scope
 * @dependency {Object} RiderService
 */
riderApp.controller('RiderController', [
    '$scope',
    'RiderService',
    function ($scope, RiderService) {
        /*
         * @property bike_types
         * @type {Array}
         */
        $scope.bike_types = [
            'Cargo',
            'Regular'
        ];

        /**
         * @method select_rider
         * @param {Int} rnumber the rider number
         * @return {None}
         */
        $scope.select_rider = function (rnumber) {
            $scope.selected = _.filter($scope.riders, function (rider) {
                return rider.number == rnumber;
            })[0];
        }

        /**
         * @method create_rider - Use the RiderService.create_rider to persist
         *     a new rider to the database
         * @return {None}
         */
        $scope.create_rider = function () {
            RiderService.create_rider($scope.new_rider).then(function (res) {
                if (res.data) {
                    $scope.riders.push(res.data);
                }
            });
        }

        /**
         * @method update_rider - User the RiderService.update_rider to update
         *     a rider data change to the database
         * @return {None}
         */
        $scope.update_rider = function () {
            console.log($scope.selected);
        }

        /**
         * On load, get all the riders
         */
        RiderService.get_riders().then(function (res) {
            $scope.riders = res.data;
        });
    }
]);

/**
 * @class RiderService
 * @dependency {Object} $http
 */
riderApp.factory('RiderService', [
    '$http',
    function ($http) {
        var RiderService = {
            /**
             * @method get_riders - ask an HTTP endpoint for all the riders
             * @return {$http Promise}
             */
            get_riders: function () {
                return $http({method: 'GET', url: '/rider/'});
            },

            /**
             * @method create_rider - make an HTTP request to create a new rider
             * @return {$http Promise}
             */
            create_rider: function (data) {
                return $http({
                    method: 'POST',
                    data: data,
                    url: '/rider/'
                });
            }
        }

        return RiderService;
    }
]);
