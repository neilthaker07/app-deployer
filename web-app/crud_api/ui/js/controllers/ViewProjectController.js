angular.module('AppDeployerDashboard')
.controller('ViewProjectController', function($scope, ProjectService, $routeParams , $location) {

  ProjectService.getProjectDetails($routeParams.projectId).then(function (response) {
    $scope.projectData = response.data;
  });



});
