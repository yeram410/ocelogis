let map, map2;

var slideIndex = 1;
showSlides(slideIndex);

function plusSlides(n) {
  showSlides(slideIndex += n);
}

function showSlides(n) {
  var i;
  var slides = document.getElementsByClassName("slides");
  if (n > slides.length) {slideIndex = 1}
  if (n < 1) {slideIndex = slides.length}
  for (i = 0; i < slides.length; i++) {
      slides[i].style.display = "none";  
  }
  slides[slideIndex-1].style.display = "block"; 
}


function processData(allText) {
  var record_num = 5;  // or however many elements there are in each row
  var allTextLines = allText.split(/\r\n|\n/);
  var entries = allTextLines[0].split(',');

  var locations = [];

  for (let i = 0; i < allTextLines.length; i ++) {
    locations.push({
      position: new google.maps.LatLng(allTextLines[i].split(',')[13], allTextLines[i].split(',')[14]),
    })
  }
  return locations;
}

function processVulnerableData(allText) {
  var record_num = 5;  // or however many elements there are in each row
  var allTextLines = allText.split(/\r\n|\n/);
  var entries = allTextLines[0].split(',');

  var locations = [];

  for (let i = 0; i < allTextLines.length; i ++) {
    let temp = allTextLines[i].split(',');
    locations.push({
      position: new google.maps.LatLng(temp[temp.length-1], temp[temp.length-2]),
    })
  }
  console.log(locations)
  return locations;
}

function initMap() {
  map = new google.maps.Map(document.getElementById("map"), {
    center: new google.maps.LatLng(36.026713543502424, 129.3660120580705),
    zoom: 14,
  });

  $.ajax({
    type: "GET",
    url: "/data/accident_area.csv",
    dataType: "text",
  }).then((data) => {
    return processData(data);
  }).then((locations) => {
    console.log(locations);
    locations.forEach((item, i) => {
      if (i < 10000) {
        const marker = new google.maps.Marker({
          position: item.position,
          icon: './images/pin22.png',
          map: map,
        });
        console.log("getting called");
      }
    })
  });

}

function hover(element, i) {
  element.setAttribute('src', 'images/'+ i + '-' + i +'.jpg');
}

function unhover(element, i) {
  element.setAttribute('src', 'images/'+ i +'.jpg');
}