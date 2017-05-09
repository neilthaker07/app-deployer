angular.module('AppDeployerDashboard')
.controller('ViewAgentsController', function($scope, ProjectService, $routeParams , $location) {

$scope.loadAgents = function() {
  ProjectService.getAgents($routeParams.projectId).then(function (response) {
    $scope.agentsList = response.data;
  });
};

$scope.loadAgents();
});
