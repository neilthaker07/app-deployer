angular.module('AppDeployerDashboard')
.controller('ViewAgentsController', function($rootScope, $scope, ProjectService, $routeParams , $location,$interval) {

$scope.loadAgents = function() {
  ProjectService.getAgents($routeParams.projectId).then(function (response) {
    $scope.agentsList = response.data;
  });
};

$interval(function() {
            $scope.loadAgents();
          }, 1000);

});
