angular.module('AppDeployerDashboard')
.controller('ViewAllProjectsController', function($scope, ProjectService, $location ) {

  ProjectService.getProject().then(function (response) {
    $scope.projectsList = response.data;
  });

  $scope.viewProject = function(projectId) {
    $location.path('project/'+projectId);
  };

  $scope.deployProject = function(id, name, url){
    ProjectService.deployProject(id, name, url).then(function(response){
      alert('Started deployment on all the registered agents (raspberry pi).');
    });
  };

    $scope.deleteProject = function(id){
      ProjectService.deleteProject(id).then(function(response){
        alert('Project deleted');
        ProjectService.getProject().then(function (response) {
          $scope.projectsList = response.data;
        });
      });
    };
});
