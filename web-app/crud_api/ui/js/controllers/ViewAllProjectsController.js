angular.module('AppDeployerDashboard')
.controller('ViewAllProjectsController', function($scope, ProjectService, $location ) {

  ProjectService.getProject().then(function (response) {
    $scope.projectsList = response.data;
  });

  $scope.viewProject = function(projectId) {
    $location.path('project/'+projectId);
  };

});
