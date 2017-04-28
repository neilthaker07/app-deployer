/**
* Main AngularJS Web Application
*/
angular.module('AppDeployerDashboard', ['ngRoute']).
config(function($routeProvider) {

    $routeProvider
    .when("/", {
      templateUrl: 'ui/partials/addProject.html',
      controller: 'AddProjectController'
    })
    .when("/allprojects", {
      templateUrl: 'ui/partials/viewAllProjects.html',
      controller: 'ViewAllProjectsController'
    })
    .when("/create", {
      templateUrl: 'ui/partials/addProject.html',
      controller: 'AddProjectController'
    });
});
/*config(['$routeProvider', function($routeProvider) {
$routeProvider
.when('/create', {
templateUrl: 'ui/partials/addProject.html',
controller: 'AddProjectController'
});
}]);*/
