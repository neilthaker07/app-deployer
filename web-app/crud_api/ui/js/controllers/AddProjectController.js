angular.module('AppDeployerDashboard')
.controller('AddProjectController', function($scope, ProjectService, $location) {

 $scope.addProject = function(){
   ProjectService.addProject($scope.projectName, $scope.githubURL).then(function(response){
     $location.path('allprojects');
   });
 };
});
