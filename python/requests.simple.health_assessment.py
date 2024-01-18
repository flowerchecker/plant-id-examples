import base64

import requests

with open('../images/unknown_plant.jpg', 'rb') as file:
    images = [base64.b64encode(file.read()).decode('ascii')]

response = requests.post(
    'https://api.plant.id/v3/health_assessment',
    params={'details': 'description,treatment'},
    headers={'Api-Key': 'your_api_key'},
    json={'images': images},
)

identification = response.json()

print('is healthy' if identification['result']['is_healthy']['binary'] else 'has disease')
for suggestion in identification['result']['disease']['suggestions']:
    print(suggestion['name'])
    print(f'probability {suggestion["probability"]:.2%}')
    print(suggestion['details']['description'])
    print(suggestion['details']['treatment'])
    print()
