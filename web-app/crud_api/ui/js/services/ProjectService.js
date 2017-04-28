angular.module('AppDeployerDashboard')
.service('ProjectService', function($http) {

  this.addProject = function(projectName, gitURL) {
    alert("Adding project "+ projectName + " " +gitURL);
    //todo: Add http post to add a project
  }

});
