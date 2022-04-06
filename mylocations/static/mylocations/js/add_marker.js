const copy = "© <a href='https://www.openstreetmap.org/copyright'>OpenStreetMap</a> contributors";
const url = "https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png";
const osm = L.tileLayer(url, { attribution: copy });
const map = L.map("map", { layers: [osm], center: [-20.211, 57.670], zoom: 10 });


let position = []
let namePos = ''

document.getElementById('map').style.cursor = 'crosshair'

map.on('click', function (e) {    
    document.getElementById('map').style.cursor = 'none'
    var marker = new L.marker(e.latlng).addTo(map);
    position.push({'lat': e.latlng.lat,'lng': e.latlng.lng})
    console.log(position)       
});

let csrfToken = document.getElementsByTagName("input")[0].value;

const submit = document.getElementById('submit');
submit.onclick = function(e){
    e.preventDefault()
    const namePos = document.getElementById("name").value;
    if(!namePos){
        console.log('empty')
    }else if(position.length==0){
        console.log('empty222')
    }else{
        console.log(namePos)
        console.log(position)
        console.log(csrfToken)
        let postData = {
            'position': position,
            'name':  namePos,
        };
        fetch("/add_marker", {
            method: "POST",
            body: JSON.stringify(postData),
            headers: {"content-type": "application/json", "X-CSRFToken": csrfToken },
        })

    }    
};