[Plant.id](https://Plant.id) offers a plant identification service based on machine learning. Once you [obtain the API key](https://web.plant.id/plant-identification-api/) you can use these client's code to speed-up the development of your implementation.

# What you'll get
For each identification requests, the API response a multiple species suggestions like this:
```json
{
  "id": 3010636,
  "plant": {
    "name": "Buddleja davidii",
    "url": "https://en.wikipedia.org/wiki/Buddleja_davidii",
    "common_name": "Butterfly-Bush"
  },
  "probability": 0.9277143686644568,
  "confidence": 0.9798141922207031,
  "similar_images": [
    {
      "id": "605775c7cb05e8463f7f8463b0fd915c",
      "similarity": 0.9318117206281141,
      "url": "https://storage.googleapis.com/plant_id_images/similar_images/2019_05/images/Buddleja davidii/605775c7cb05e8463f7f8463b0fd915c.jpg",
      "url_small": "https://storage.googleapis.com/plant_id_images/similar_images/2019_05/images/Buddleja davidii/605775c7cb05e8463f7f8463b0fd915c.small.jpg"
    },
    {
      "id": "890cf5e5b94a255ea4e517d785f53481",
      "similarity": 0.9316171609752804,
      "url": "https://storage.googleapis.com/plant_id_images/similar_images/2019_05/images/Buddleja davidii/890cf5e5b94a255ea4e517d785f53481.jpg",
      "url_small": "https://storage.googleapis.com/plant_id_images/similar_images/2019_05/images/Buddleja davidii/890cf5e5b94a255ea4e517d785f53481.small.jpg"
    }
  ],
  "confirmed": false
}
```
Those "similar images" are representative images of the identified species carefully selected by the model so it resembles the input image.

# API reference
 * [api.plant.id/identify](https://plantid.docs.apiary.io/#reference/0/identification/identify-plant) – sends plant photos to our backend, queue the request and returns its identification
 * [api.plant.id/check-identifications](https://plantid.docs.apiary.io/#reference/0/check/check-identifications) – checks if identification has been already proceeded and eventually returns the result of the identification
 
The result of the identification is a list of records showing possible plant species (taxons). Each record contains: the scientific name of the plant, probability (certainty level), representative images of the suggested taxon, common name and/or URL.
 
See https://plantid.docs.apiary.io for full reference.

# Python example

See [python](https://github.com/Plant-id/plant-id-examples/blob/master/python/plant_id_client.py) file

# Android/java example

See [android](https://github.com/Plant-id/plant-id-examples/tree/master/android) directory
