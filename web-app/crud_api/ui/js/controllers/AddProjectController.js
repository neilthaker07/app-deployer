angular.module('AppDeployerDashboard')
.controller('AddProjectController', function($scope, ProjectService ) {

 $scope.addProject = function(){
   ProjectService.addProject($scope.projectName, $scope.githubURL);
 }
});
