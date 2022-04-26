const https = require('https')
var fs = require('fs');

const files = ['../img/photo1.jpg', '../img/photo2.jpg', '../img/photo3.jpg'];

const base64files = files.map(file => fs.readFileSync(file, 'base64'));

const data = JSON.stringify({
    api_key: "-- ask for one: https://web.plant.id/api-access-request/ --",
    images: base64files,
    /* modifiers info: https://github.com/flowerchecker/Plant-id-API/wiki/Modifiers */
    modifiers: ["crops_fast", "similar_images"],
    language: "en",
    /* disease details info: https://github.com/flowerchecker/Plant-id-API/wiki/Disease-details */
    disease_details: ["cause",
        "common_names",
        "classification",
        "description",
        "treatment",
        "url"],
});

const options = {
    hostname: 'api.plant.id',
    port: 443,
    path: '/v2/health_assessment',
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