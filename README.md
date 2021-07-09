[Plant.id](https://web.plant.id) offers a plant identification service based on machine learning. Once you [obtain the API key](https://web.plant.id/plant-identification-api/), you can use these client's code to speed-up the development of your implementation.

# Plant.id API v2

## Documentation
See our [documentation](https://github.com/Plant-id/Plant-id-API/wiki) for the full reference.

## Simple Python example
```python
import base64
import requests

# encode image to base64
with open("unknown_plant.jpg", "rb") as file:
    images = [base64.b64encode(file.read()).decode("ascii")]

your_api_key = "fd3slj47dj... -- ask for one: https://web.plant.id/api-access-request/ --"
json_data = {
    "images": images,
    "modifiers": ["similar_images"],
    "plant_details": ["common_names", "url", "wiki_description", "taxonomy"]
}

response = requests.post(
    "https://api.plant.id/v2/identify",
    json=json_data,
    headers={
        "Content-Type": "application/json",
        "Api-Key": your_api_key
    }).json()

for suggestion in response["suggestions"]:
    print(suggestion["plant_name"])    # Taraxacum officinale
    print(suggestion["plant_details"]["common_names"])    # ["Dandelion"]
    print(suggestion["plant_details"]["url"])    # https://en.wikipedia.org/wiki/Taraxacum_officinale
```

## More examples
- [Python example - synchronous](https://github.com/Plant-id/Plant-id-API/blob/master/python/sync_identification_example.py)
- [Python example - asynchronous](https://github.com/Plant-id/Plant-id-API/blob/master/python/async_identification_example.py)
- [Java example](https://github.com/Plant-id/Plant-id-API/tree/master/java)
- [JavaScript example](https://github.com/Plant-id/Plant-id-API/blob/master/javascript/sync_identification_example.html)
- [node.js example](https://github.com/Plant-id/Plant-id-API/tree/master/node)
- [PHP example](https://github.com/Plant-id/Plant-id-API/blob/master/php/sync_identification_example.php)
- [Rust example](https://github.com/Plant-id/Plant-id-API/tree/master/rust/async)
- [React Native example](https://github.com/Plant-id/Plant-id-API/tree/master/react-native)

Don't know how to code? Try the [online demo](https://plant.id/).
