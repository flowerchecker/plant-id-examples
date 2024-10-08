import base64

import requests

with open('../images/unknown_plant.jpg', 'rb') as file:
    images = [base64.b64encode(file.read()).decode('ascii')]

# suggestion_filter - dict (optional) in format {"classification": "FILTER_NAME (filter examples below)"} Restricts
# the output of the model to specified list of classes (region or plant type) and adjusts the probabilities. The
# lists can be combined with logical operators and parentheses. The lists are available here:
# https://plant.id/suggestion_filters
#
# Examples:
# Vegetables - {"classification": "vegetable"}
# Houseplants and wild plants in Europe - {"classification": "houseplant OR continent__europe"}
# Trees in Europe and North America - {"classification": "(continent__northern_america OR continent__europe) AND tree"}

suggestion_filter = {'classification': '(continent__northern_america OR continent__australasia) AND Succulent'}

response = requests.post(
    'https://api.plant.id/v3/identification',
    params={'details': 'url,common_names'},
    headers={'Api-Key': 'your_api_key'},
    json={'images': images, 'suggestion_filter': suggestion_filter},
)

identification = response.json()

print('is plant' if identification['result']['is_plant']['binary'] else 'is not plant')
for suggestion in identification['result']['classification']['suggestions']:
    print(suggestion['name'])
    print(f'probability {suggestion["probability"]:.2%}')
    print(suggestion['details']['url'], suggestion['details']['common_names'])
    print()
