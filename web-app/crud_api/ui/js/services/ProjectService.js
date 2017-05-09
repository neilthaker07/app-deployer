angular.module('AppDeployerDashboard')
.service('ProjectService', function($http, UserService) {

  this.addProject = function(projectName, gitURL) {
    return $http.post("/v1/" + UserService.getUserName() + "/projects", {"projectName":projectName, "projectUrl":gitURL});
    //todo: Add http post to add a project
  };

  this.getProject = function() {
    return $http.get("/v1/" + UserService.getUserName() + "/projects");
  };

  this.getProjectDetails = function(projectId) {
    return $http.get("/v1/" + UserService.getUserName() + "/projects/" + projectId);
  };

  this.deployProject = function(id, name, url) {
    return $http.post("/v1/" + UserService.getUserName() + "/projects/" + id +"/deploy", {"url":url});
  };

  this.deleteProject = function(id) {
    return $http.delete("/v1/" + UserService.getUserName() + "/projects/" + id);
  };

  this.getAgents = function(projectId) {
    return $http.get("/v1/" + UserService.getUserName() + "/projects/" + projectId + "/agents");
  };
});
