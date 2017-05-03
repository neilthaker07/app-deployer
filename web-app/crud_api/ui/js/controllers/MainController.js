angular.module('AppDeployerDashboard')
.controller('MainController', function($scope, $location) {

$scope.go = function(path) {
  $location.path(path);
};
});
