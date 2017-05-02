angular.module('AppDeployerDashboard')
.controller('ViewAllProjectsController', function($scope, ProjectService ) {

  ProjectService.getProject().then(function (response) {
    $scope.projectsList = response.data;
  });

});
