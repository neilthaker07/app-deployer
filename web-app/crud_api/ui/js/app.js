/**
* Main AngularJS Web Application
*/
angular.module('AppDeployerDashboard', ['ngRoute']).
config(function($routeProvider) {

    $routeProvider
    .when("/", {
      templateUrl: 'ui/partials/login.html',
      controller: 'LoginController'
    })
    .when("/allprojects", {
      templateUrl: 'ui/partials/viewAllProjects.html',
      controller: 'ViewAllProjectsController'
    })
    .when("/create", {
      templateUrl: 'ui/partials/addProject.html',
      controller: 'AddProjectController'
    });
})
.run(function($rootScope, UserService, $location) {
  if (!UserService.getUserName()) {
    $location.path('/');
  }
  $rootScope.$on('$routeChangeStart', function(next, current) {
   if (!UserService.getUserName()) {
     $location.path('/');
   }
 });
});;
/*config(['$routeProvider', function($routeProvider) {
$routeProvider
.when('/create', {
templateUrl: 'ui/partials/addProject.html',
controller: 'AddProjectController'
});
}]);*/
