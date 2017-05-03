angular.module('AppDeployerDashboard')
.controller('NewUserController', function($scope, UserService , $location) {

 $scope.register = function(){
   $scope.registerFailureMessage = null;
   UserService.register($scope.unm, $scope.pwd).then(function(response){
       UserService.setUserName($scope.unm);
       $location.path('create');
   },
 function(response){
    $scope.registerFailureMessage = response.data;
 });
 };

$scope.alreadyRegistered = function(){
  $location.path('login');
}

});
