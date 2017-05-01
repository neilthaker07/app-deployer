angular.module('AppDeployerDashboard')
.service('ProjectService', function($http, UserService) {

  this.addProject = function(projectName, gitURL) {
    alert("Adding project "+ projectName + " " +gitURL + " for user " + UserService.getUserName());
    //todo: Add http post to add a project
  };

  this.getProject = function() {
    alert("Get projects for user " + UserService.getUserName());
  };

});
