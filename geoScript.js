var geocoder = new google.maps.Geocoder();
var directionsService = new google.maps.DirectionsService();
var directionsDisplay = new google.maps.DirectionsRenderer();
var map;
var log = function(log){
    console.log(log);
}
// Initializer
// CHANGE: center according to arena
var initMap = function () {
    var mapEl = document.getElementById('container');
    var mapProp = {
        center: new google.maps.LatLng(29.564904, -95.0814),
        zoom: 19
        //mapTypeId: google.maps.MapTypeId.SATELLITE
    };
    map = new google.maps.Map(mapEl, mapProp);
};
var plotRoute = function(){
    
    // CHANGE:
    // 51, -0.12 is a dummy lattitude and longitude
    // plotRoute can be parameterized using start and end
    var start = new google.maps.LatLng(51, -0.12);
    var end = new google.maps.LatLng(51.5, -0.12);

    // Request object
    var request = {
      origin: start,
      destination: end,
      travelMode: google.maps.TravelMode.DRIVING
    };
    directionsService.route(request, function(response, status) {
      if (status == google.maps.DirectionsStatus.OK) {
        directionsDisplay.setDirections(response);
        directionsDisplay.setMap(map);
      } else {
        console.error("Directions Request Failed");
      }
    });
};

// Plots a pin on the Map
// Can be used if we dont need to plot a route but series of pins
var showMarker = function(latlang){
    marker = new google.maps.Marker({
        position: latlang,
        map: map
        // title: result.formatted_address
    });
    map.panTo(marker.getPosition());
};

var resetSize = function(width, height){
    var container = document.getElementById("container")
    container.style.width = "" + width + "px"
    container.style.height = "" + height + "px" 
}

var init = function () {
    log("start");
    initMap();
    //plotRoute();
}

document.addEventListener("DOMContentLoaded",init,false);
