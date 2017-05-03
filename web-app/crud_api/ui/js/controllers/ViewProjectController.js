angular.module('AppDeployerDashboard')
.controller('ViewProjectController', function($scope, ProjectService, $routeParams , $location) {

console.log($routeParams);
console.log($routeParams.projectId);
  ProjectService.getProjectDetails($routeParams.projectId).then(function (response) {
    console.log(response);
    $scope.projectData = response.data;
  });



});
