[Plant.id](https://plant.id) offers a plant identification service based on machine learning. Once you [obtain the API key](https://web.plant.id/plant-identification-api/), you can use these client's code to speed-up the development of your implementation.

# Plant.id API v2

## Identify your plant
Send plant photos to our back end, wait for identification, and return the result. If the identification takes more than the `identification_timeout`, return identification info without any suggestions.

### Request
Send POST request to: `https://api.plant.id/v2/identify` and include following parameters:

- **`api_key`**- your [API key](https://web.plant.id/plant-identification-api/)
- **`images`** - one ore more images of the plant you want to identify (string - base64 or a file)

Other optional parameters:
- `modifiers` - list of strings: 
    - `"crops_simple"`/`"crops_fast"` (default)/`"crops_medium"` - specify the speed & accuracy of the identification
    - `"similar_images"` - allow displaying of similar images -> **If you want to get similar images in the response, you must include item `similar_images` here.**
- `plant_language` - language code ([ISO 639-1](https://en.m.wikipedia.org/wiki/List_of_ISO_639-1_codes)) used for `plant_details` (default `"en"`)
- `plant_details` - list of strings, which determines which information about the plant will be included in the response (if the data is available)
    - `"common_names"` - list of common names of the plant in the language specified in `plant_language`
    - `"url"` - link to page with the plant profile (usually Wikipedia)
    - `"name_authority"` - scientific name of the plant
    - `"wiki_description"` - description of the plant from Wikipedia with source url and license
    - `"taxonomy"` - dictionary with the plant taxonomy
- and more (see the [Documentation](https://github.com/Plant-id/Plant-id-API/wiki/Synchronous-identification))

### Response
The result contains a list of suggestions of possible plant species (taxons). Each suggestion contains:
- `scientific_name` - the scientific name of the plant
- `common_names` - list of common names of the plant (if available)
- `url` - link to page with the plant profile (usually Wikipedia)
- `wiki_description` - description of the plant from Wikipedia (if available)
- `taxonomy` - taxonomy of the plant (if available)
- `probability` - certainty level that suggested plant is the one from the photo
- `similar_images` - representative images of the identified species carefully selected by the model, so it resembles the input image (Similar images are included in the result only if you add the value `similar_image` in the `modifiers` list of the request.)
- and more (see the [Documentation](https://github.com/Plant-id/Plant-id-API/wiki/Synchronous-identification))

## Try it yourself!
We prepared a simple code to demostrate, how the API works. See the [Python example](https://github.com/Plant-id/Plant-id-API/blob/master/python/sync_identification_example.py)

## Documentation
See our [documentation](https://github.com/Plant-id/Plant-id-API/wiki) for full reference.
