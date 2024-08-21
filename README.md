[Plant.id](https://www.kindwise.com/plant-id) by [kindwise](https://kindwise.com) offers [plant identification](https://www.kindwise.com/plant-id)
and [plant diseases identification](https://www.kindwise.com/plant-health) API based on machine learning. 
Once you [register and obtain the API key](https://admin.kindwise.com/signup), you can use these client's code available in this repository to speed-up the development of your implementation.

# Plant.id API v3

 - **[documentation](https://plant.id/docs)** - full API reference
 - **[python SDK](https://github.com/flowerchecker/kindwise-api-client)** - simply use API from python
 - API specification on **[Postman](https://www.postman.com/winter-shadow-932363/workspace/kindwise/collection/24599534-c4a4048d-ed97-4532-8980-3159ddbfe629)**
 - try [online demo](https://plant.id/)
 - more [python examples](python)

## Plant Identification 🌱

Submit images of plants and get a list of possible species suggestions along with detailed information.

```bash
pip install kindwise-api-client
```

```python
from kindwise import PlantApi

api = PlantApi('your_api_key')
identification = api.identify('../images/unknown_plant.jpg', details=['url', 'common_names'])

print('is plant' if identification.result.is_plant.binary else 'is not plant')
for suggestion in identification.result.classification.suggestions:
    print(suggestion.name)
    print(f'probability {suggestion.probability:.2%}')
    print(suggestion.details['url'], suggestion.details['common_names'])
    print()
```

Same example in pure python

```python
import base64

import requests

with open('../images/unknown_plant.jpg', 'rb') as file:
    images = [base64.b64encode(file.read()).decode('ascii')]

response = requests.post(
    'https://api.plant.id/v3/identification',
    params={'details': 'url,common_names'},
    headers={'Api-Key': 'your_api_key'},
    json={'images': images},
)

identification = response.json()

print('is plant' if identification['result']['is_plant']['binary'] else 'is not plant')
for suggestion in identification['result']['classification']['suggestions']:
    print(suggestion['name'])
    print(f'probability {suggestion["probability"]:.2%}')
    print(suggestion['details']['url'], suggestion['details']['common_names'])
    print()

```


## Health Assessment 🥀

Submit photos of sick plants, and receive a list of potential health issues.

```Python
from kindwise import PlantApi

api = PlantApi('your_api_key')
identification = api.health_assessment('../images/unhealthy_plant.jpg', details=['description', 'treatment'])

print('is healthy' if identification.result.is_healthy.binary else 'has disease')
for suggestion in identification.result.disease.suggestions:
    print(suggestion.name)
    print(f'probability {suggestion.probability:.2%}')
    print(suggestion.details['description'])
    print(suggestion.details['treatment'])
    print()
```

## Conversation 🤖 💬

Chat about identification with ChatBot. ChatBot supports multiple backends and its configuration can be modified.

```Python
from kindwise import PlantApi, MessageType

api = PlantApi('your_api_key')
conversation = api.ask_question('plant identification', 'Is this plant edible?')

for message in conversation.messages:
    if message.type == MessageType.ANSWER:
        print(f'App: {message.content}')
    else:
        print(f'Client: {message.content}')
    print()
print('Feedback:', conversation.feedback.get('rating'))
```
