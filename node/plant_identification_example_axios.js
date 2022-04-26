const axios = require('axios')
var fs = require('fs');

const files = ['../img/photo1.jpg', '../img/photo2.jpg', '../img/photo3.jpg'];

const base64files = files.map(file => fs.readFileSync(file, 'base64'));

const data = {
    api_key: "-- ask for one: https://web.plant.id/api-access-request/ --",
    images: base64files,
    /* modifiers docs: https://github.com/flowerchecker/Plant-id-API/wiki/Modifiers */
    modifiers: ["crops_fast", "similar_images"],
    plant_language: "en",
    /* plant details docs: https://github.com/flowerchecker/Plant-id-API/wiki/Plant-details */
    plant_details: ["common_names",
        "url",
        "name_authority",
        "wiki_description",
        "taxonomy",
        "synonyms"],
};

axios.post('https://api.plant.id/v2/identify', data).then(res => {
    console.log('Success:', res.data);
}).catch(error => {
    console.error('Error: ', error)
})