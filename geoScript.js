var geocoder = new google.maps.Geocoder();
var directionsService = new google.maps.DirectionsService();
var directionsDisplay = new google.maps.DirectionsRenderer();
var map;
var markers = [];
var markerColor = "Purple";
function log(log){
    console.log(log);
}
// Initializer
// CHANGE: center according to arena
function initMap() {
    var mapEl = document.getElementById('container');
    var mapProp = {
        center: new google.maps.LatLng(29.564904, -95.0814),
        zoom: 19
        //mapTypeId: google.maps.MapTypeId.SATELLITE
    };
    map = new google.maps.Map(mapEl, mapProp);
    map.addListener('rightclick', function(e) {
        showCircle(e.latLng);
    });
}

function plotRoute() {
    
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
}

// Plots a pin on the Map
// Can be used if we dont need to plot a route but series of pins
function showMarker(latlng) {
    marker = new google.maps.Marker({
        position: latlng,
        map: map
        //color: markerColor
        // title: result.formatted_address
    });
    map.panTo(marker.getPosition());
}

//Using circles to allow for different colors
function showCircle(latlng) {
    var markerCircle = new google.maps.Circle({
        strokeColor: markerColor,
        strokeOpacity: 1,
        strokeWeight: 1,
        fillColor: markerColor,
        fillOpacity: 1,
        map: map,
        center: latlng,
        radius: 1.5
    });
    markerCircle.addListener('rightclick', function(e) {
        markerCircle.setMap(null);
        var index = markers.indexOf(markerCircle);
        markers.splice(index, 1);
    });
    markers.push(markerCircle); 
}

function setMarkerColor(color) {
    markerColor = color;
}

function clearScreen(clearType) {
    log("reached1");
    if(clearType === "Markers" || clearType === "All") { 
        log("Reached2")
        for(var i = 0; i < markers.length; i++) {
            log("Reached3")
            markers[i].setMap(null);
        }
        markers = []
    }
    if(clearType === "Route" || clearType === "All") {

    }
}

function saveMarkers() {

}

function resetSize(width, height){
    var container = document.getElementById("container");
    container.style.width = "" + width + "px";
    container.style.height = "" + height + "px"; 
}

function init() {
    log("start");
    initMap();
    //plotRoute();
}

document.addEventListener("DOMContentLoaded",init,false);
