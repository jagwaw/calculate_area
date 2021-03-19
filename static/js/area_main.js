var app = angular.module('areaProject', ['ngMaterial', 'ngSanitize',  'ngRoute', 'toastr']);
// ngMaterialDateRangePicker
app.config(function ($routeProvider) {
  $routeProvider
    .when("/", {
      templateUrl: "area.html"
    })
  
});


app.controller("areaController", function ($scope, $http, $log,  toastr, $filter) {
  $scope.shape_list=["Circle","Square","Triangle","Rectangle"]
  $scope.measurement_list=["centimeters","inches","meters"]
  $scope.shape="Circle"
  $scope.selected_shape="Circle"

  $scope.my_regex = /^([1-9]|[1-5][0-9]|60(\.0{1,2})?$)(\.[0-9]{1,2})?$/

  $scope.checkShape= function(shape){
    $scope.selected_shape=shape
    $scope.calculated_area=''
    $scope.calculated_measurement=''
  }
  $scope.area_params={}
  $scope.area_params.radius=""
  $scope.area_params.radius_measurement=""
  $scope.area_params.base=""
  $scope.area_params.base_measurement=""
  $scope.area_params.height=""
  $scope.area_params.height_measurement=""
  $scope.area_params.side=""
  $scope.area_params.side_measurement=""
  $scope.area_params.length=""
  $scope.area_params.length_measurement=""
  $scope.area_params.width=""
  $scope.area_params.width_measurement=""
  $scope.output_measurement="centimeters"

  $scope.calculateArea= function(){
    $scope.proceed_compute=true
    if($scope.output_measurement == ''){
      toastr.error("Please select the measurement.")
      $scope.proceed_compute=false
    } 
    else{
      $scope.area_params.output_measurement=$scope.output_measurement
    }
    if($scope.selected_shape == ''){
      toastr.error("Please select the shape.")
      $scope.proceed_compute=false
    } 

    else{
      if($scope.selected_shape == 'Circle'){
          $scope.area_params.shape=$scope.shape
          if($scope.area_params.radius == '' || $scope.area_params.radius_measurement == '' ){
              toastr.error("Please enter or select the corresponding value in the field.")
              $scope.proceed_compute=false

          }
      }
      if($scope.selected_shape == 'Triangle'){
          $scope.area_params.shape=$scope.shape
          if(($scope.area_params.base == '' || $scope.area_params.height == '' ) || ($scope.area_params.base_measurement == '' || $scope.area_params.height_measurement == '' )){
            toastr.error("Please enter or select the corresponding value in the field.")
            $scope.proceed_compute=false
          }
      }
      if($scope.selected_shape == 'Square'){
          $scope.area_params.shape=$scope.shape
          if($scope.area_params.side == '' || $scope.area_params.side_measurement == '' ){
            toastr.error("Please enter the side.")
            $scope.proceed_compute=false
          }
      }
      if($scope.selected_shape == 'Rectangle'){
          $scope.area_params.shape=$scope.shape
          if(($scope.area_params.length == '' || $scope.area_params.width == '' )  || ($scope.area_params.length_measurement == '' || $scope.area_params.width_measurement == '' )){
            toastr.error("Please enter the corresponding value in the input field.")  
            $scope.proceed_compute=false
          }
      }
    }   
    if($scope.proceed_compute == true){
      $log.info($scope.area_params)

      $http({
        url: "/falcon/area/compute",
        method: "POST",
        data: $scope.area_params
      }).then(function (response) {
        $log.info(response.data)
        $scope.calculated_area=''
        $scope.calculated_measurement=''
        $scope.calculated_area = response.data["area"]
        $scope.calculated_measurement=response.data["measurement"]
        
      })
    }

  }

})