// app.js

var app = angular.module('imgur', []);

app.config(['$httpProvider', function($httpProvider) {
        $httpProvider.defaults.useXDomain = true;
    }
]);

app.controller('imgurController', ['$scope', '$location', '$http', function($scope, $location, $http) {

    $scope.getImages = function (callback) {

        url = $location.absUrl() + 'getimage'
        $http.get(url).then(function (res) {
            arr = angular.fromJson(res).data.data
            sorted = arr.sort(function (a, b) {
                if (a.datetime < b.datetime) {
                    return 1
                }
            })
            console.log(sorted)
            img = sorted[0]
            for (var i = 0; i < sorted.length; i++) {
                if (img.privacy == 'hidden' || img.privacy == 'private') {
                    continue
                } else {
                    img = sorted[i]
                    break
                }
            }
            $scope.imgTitle = img.title
            $scope.imgAuthor = img.account_url
            if (img.description == null) {
                $scope.imgDesc = ''
            } else {
                $scope.imgDesc = img.description
            }
            $scope.imgStats = img.score
            $scope.imgLink = img.link
            console.log(img)
            if (img.cover) {
                $scope.getSingleImage(img.cover, function (imgURI) {
                    $scope.newImage = imgURI
                    console.log($scope.newImage)
                    return callback()
                })
            } else {
                $scope.newImage = img.link
                return callback()
            }

        })
    }

    $scope.getSingleImage = function (id, callback) {
        $http.get($location.absUrl() + 'getimageuri/' + id).then(function (i) {
            r = angular.fromJson(i).data.data.link
            return callback(r)
        })    
    }


    $scope.getImages(function () {
        console.log('done')
    })


}]);