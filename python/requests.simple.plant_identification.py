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
