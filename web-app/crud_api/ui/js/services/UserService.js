angular.module('AppDeployerDashboard')
.service('UserService', function($http) {

  var userName = 'nishant';

  this.getUserName = function() {
    return userName;
  };

  this.login = function(username, password) {
    //todo: add ajax call to validate usnm and pwd
  };

});
