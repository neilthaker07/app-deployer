angular.module('AppDeployerDashboard')
.service('UserService', function($http) {

  var userName = null;

  this.getUserName = function() {
    return userName;
  };

  this.setUserName = function(username) {
    return userName = username;
  };

  this.login = function(username, password) {
    return $http.post("/v1/userLogin",{"username":username, "password":password});
  };

  this.register = function(username, password) {
    return $http.post("/v1/userSignup",{"username":username, "password":password});
  };

});
