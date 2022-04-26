const axios = require('axios')
var fs = require('fs');

const files = ['../img/photo1.jpg', '../img/photo2.jpg', '../img/photo3.jpg'];

const base64files = files.map(file => fs.readFileSync(file, 'base64'));

const data = {
    api_key: "-- ask for one: https://web.plant.id/api-access-request/ --",
    images: base64files,
    /* modifiers docs: https://github.com/flowerchecker/Plant-id-API/wiki/Modifiers */
    modifiers: ["crops_fast", "similar_images"],
    language: "en",
    /* disease details docs: https://github.com/flowerchecker/Plant-id-API/wiki/Disease-details */
    disease_details: ["cause",
        "common_names",
        "classification",
        "description",
        "treatment",
        "url"],
};

axios.post('https://api.plant.id/v2/health_assessment', data).then(res => {
    console.log('Success:', res.data);
}).catch(error => {
    console.error('Error: ', error)
})