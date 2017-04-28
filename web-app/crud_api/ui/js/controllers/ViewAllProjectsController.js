angular.module('AppDeployerDashboard')
.controller('ViewAllProjectsController', function($scope, ProjectService ) {

   ProjectService.getProject();

});
