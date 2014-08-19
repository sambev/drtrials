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
         */
        $scope.select_rider = function (rnumber) {
            $scope.selected = _.filter($scope.riders, function (rider) {
                return rider.number == rnumber;
            })[0];
        }

        /**
         * @method create_rider - Use the RiderService.create_rider to persist
         *     a new rider to the database
         */
        $scope.create_rider = function () {
            RiderService.create_rider($scope.new_rider).then(
                function (res) {
                    $scope.create_success = true;
                    $scope.create_error = '';
                    $scope.riders.push(res.data[0]);
                },
                function (res) {
                    $scope.create_success = false;
                    $scope.create_error = res.data.msg;
                }
            );
        }

        /**
         * @method update_rider - User the RiderService.update_rider to update
         *     a rider data change to the database
         */
        $scope.update_rider = function () {
            RiderService.update_rider($scope.selected).then(
                function (res) {
                    $scope.update_success = true;
                    $scope.update_error = '';
                },
                function (res) {
                    $scope.update_success = false;
                    $scope.update_error = res.data.msg;
                }
            );
        }

        $scope.delete_rider = function (number) {
            var to_delete = _.find($scope.riders, function (rider) {
                return rider.number == number;
            });

            RiderService.delete_rider(to_delete).then(
                function (res) {
                    _.remove($scope.riders, function (rider) {
                        return rider.number == number;
                    });
                },
                function (res) {
                    console.error('Failed to delete user', res);
                }
            );
        }

        /**
         * @method  clear_errors - clear out the error on the scope
         * @return {[type]} [description]
         */
        $scope.clear_notifications = function () {
            $scope.create_error = '';
            $scope.update_error = '';
            $scope.create_success = '';
            $scope.update_success = '';
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
             * @param {Object} data - Rider object
             * @return {$http Promise}
             */
            create_rider: function (data) {
                var req = $http({
                    method: 'POST',
                    data: data,
                    url: '/rider/'
                });

                return req;
            },

            /**
             * @method create_rider - make an HTTP request to create a new rider
             * @param {Object} data Rider object
             * @return {$http Promise}
             */
            update_rider: function (data) {
                var req = $http({
                    method: 'PUT',
                    data: data,
                    url: '/rider/' + data._id.$oid
                });

                return req;
            },

            /**
             * method delete_rider - make an HTTP request to delete a rider
             * @param {Object} data
             * @return {$http Promise}
             */
            delete_rider: function (data) {
                var req = $http({
                    method: 'DELETE',
                    url: '/rider/' + data._id.$oid
                });

                return req;
            }
        }

        return RiderService;
    }
]);
