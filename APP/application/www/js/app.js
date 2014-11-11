   angular.module('app', ['onsen']);

   angular.module('app').controller('AppController', function($scope) {
    $scope.posts = []
    $.get("http://127.0.0.1:5000/listing", function(data){
  alert("Data: " + data);
});

    $scope.doSomething = function() {
        setTimeout(function() {
          alert('tapped');
      }, 100);
    };
    $scope.showNewListingModal = function() {
        newListingModal.show();
    };
    $scope.addListing = function() {
        if(!$scope.title || $scope.title === '' ||!$scope.description || $scope.description === '') { return; }
        $scope.posts.push({title: $scope.title, description: $scope.description});
        $scope.title = '';
        $scope.description = '';
        setTimeout('newListingModal.hide()', 500);
    };
});
