[Plant.id](https://Plant.id) offers a plant identification service based on machine learning. Once you [obtain the API key](https://web.plant.id/plant-identification-api/) you can use these client's code to speed-up the development of your implementation. 

# API reference
 * [api.plant.id/identify](https://plantid.docs.apiary.io/#reference/0/identification/identify-plant) – sends plant photos to our backend, queue the request and returns it’s identificator
 * [api.plant.id/check-identifications](https://plantid.docs.apiary.io/#reference/0/check/check-identifications) – checks if identification has been already proceed and eventually returns the result of the identification
 
Result of the identification is a list of records showing possible plant species (taxons). Each records contains: scientific name of the plant, probability (certainty level), representative images of the suggested taxon, common name and/or url.
 
See https://plantid.docs.apiary.io for full reference.

# Python example

See [python](https://github.com/Plant-id/plant-id-examples/blob/master/python/plant_id_client.py) file

# Android/java example

See [android](https://github.com/Plant-id/plant-id-examples/tree/master/android) directory
