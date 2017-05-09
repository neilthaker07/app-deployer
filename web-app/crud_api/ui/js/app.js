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
    .when("/newUser", {
      templateUrl: 'ui/partials/newUser.html',
      controller: 'NewUserController'
    })
    .when("/allprojects", {
      templateUrl: 'ui/partials/viewAllProjects.html',
      controller: 'ViewAllProjectsController'
    })
    .when("/project/:projectId", {
      templateUrl: 'ui/partials/viewProject.html',
      controller: 'ViewProjectController'
    })
    .when("/project/:projectId/agents", {
      templateUrl: 'ui/partials/viewAgents.html',
      controller: 'ViewAgentsController'
    })
    .when("/create", {
      templateUrl: 'ui/partials/addProject.html',
      controller: 'AddProjectController'
    })
    .otherwise({
      templateUrl: 'ui/partials/login.html',
      controller: 'LoginController'
    });
})
.run(function($rootScope, UserService, $location) {
  if (!UserService.getUserName()) {
    $location.path('/');
  }
  $rootScope.$on('$routeChangeStart', function(next, current) {
     if ($location.path()!='/newUser' && !UserService.getUserName()) {
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
