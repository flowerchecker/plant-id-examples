const https = require('https')
var fs = require('fs');

const files = ['../images/photo1.jpg', '../images/photo2.jpg', '../images/photo3.jpg'];

const base64files = files.map(file => fs.readFileSync(file, 'base64'));

const data = JSON.stringify({
    api_key: "-- ask for one: https://web.plant.id/api-access-request/ --",
    images: base64files,
    /* modifiers info: https://github.com/flowerchecker/Plant-id-API/wiki/Modifiers */
    modifiers: ["crops_fast", "similar_images"],
    plant_language: "en",
    /* plant details info: https://github.com/flowerchecker/Plant-id-API/wiki/Plant-details */
    plant_details: ["common_names",
        "url",
        "name_authority",
        "wiki_description",
        "taxonomy",
        "synonyms"],
});

const options = {
    hostname: 'api.plant.id',
    port: 443,
    path: '/v2/identify',
    method: 'POST',
    headers: {
        'Content-Type': 'application/json',
        'Content-Length': data.length
    }
}

const req = https.request(options, res => {
    res.on('data', d => {
        process.stdout.write(d)
    });
});

req.on('error', error => {
    console.error('Error: ', error)
});

req.write(data)

req.end()
