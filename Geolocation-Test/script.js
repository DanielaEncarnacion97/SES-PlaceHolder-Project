var button = document.getElementById("demo");

function getLocation() {
    if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(showPosition);
    } else {
        x.innerHTML = "Geolocation is not supported by this browser.";
    }
}

function showPosition(position) {
    button.innerHTML = "Latitude: " + position.coords.latitude + "<br>Longitude: " + position.coords.longitude;
    key = 'e369a55460e652';
    latitude = position.coords.latitude;
    longitude = position.coords.longitude;
    url = `https://us1.locationiq.com/v1/reverse.php?key=${key}&lat=${latitude}&lon=${longitude}&format=json`

    fetch(url)
        .then(response => {
            return response.json()
        })
        .then((data) => {
            city = data.address.city;
            county = data.address.county;
            state = data.address.state;
            country = data.address.country;
            button.innerHTML += `<br/>${city}, ${county}, ${state}, ${country}`;
        });
}
