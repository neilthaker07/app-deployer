angular.module('AppDeployerDashboard')
.controller('LoginController', function($scope, UserService , $location) {

 $scope.login = function(){
   $scope.loginFailureMessage = null;
   UserService.login($scope.unm, $scope.pwd).then(function(response){
     UserService.setUserName($scope.unm);
       $location.path('allprojects');
   }, function(response){
       $scope.loginFailureMessage = response.data.response;
   });
 };

$scope.newUser = function(){
  $location.path('newUser');
}

});
