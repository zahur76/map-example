const copy = "© <a href='https://www.openstreetmap.org/copyright'>OpenStreetMap</a> contributors";
const url = "https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png";
const osm = L.tileLayer(url, { attribution: copy });
const map = L.map("map", { layers: [osm], center: [-20.211, 57.670], zoom: 10 });


async function load_markers() {
    const markers_url = `/markers`    
    const response = await fetch(markers_url)
    const geojson = await response.json()
    console.log(geojson.features)
    return geojson
}

async function render_markers() {
    const markers = await load_markers();
    // console.log(markers)
    L.geoJSON(markers)
    .bindPopup((layer) => layer.feature.properties.name)
    .addTo(map);
}

render_markers()
