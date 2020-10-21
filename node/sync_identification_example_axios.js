const axios = require('axios')
var fs = require('fs');

const files = ['photo1.jpg', 'photo2.jpg'];

const base64files = files.map(file => fs.readFileSync(file, 'base64'));

const data = {
    api_key: "-- ask for one: https://web.plant.id/api-access-request/ --",
    images: base64files,
    modifiers: ["crops_fast", "similar_images"],
    plant_language: "en",
    plant_details: ["common_names",
        "url",
        "name_authority",
        "wiki_description",
        "taxonomy",
        "synonyms"]
};

axios.post('https://api.plant.id/v2/identify', data).then(res => {
    console.log('Success:', res.data);
}).catch(error => {
    console.error('Error: ', error)
})