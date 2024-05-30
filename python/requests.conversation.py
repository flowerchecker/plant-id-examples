import base64

import requests


with open('../images/unknown_plant.jpg', 'rb') as file:
    images = [base64.b64encode(file.read()).decode('ascii')]


def print_conversation(conversation):
    for message in conversation['messages']:
        if message['type'] == 'question':
            print(f'App: {message["content"]}')
        else:
            print(f'Client: {message["content"]}')
        print()
    print('Feedback:', conversation.get('feedback', {}).get('rating'))


def print_identification(identification):
    print('is plant' if identification['result']['is_plant']['binary'] else 'is not plant')
    for suggestion in identification['result']['classification']['suggestions']:
        print(suggestion['name'])
        print(f'probability {suggestion["probability"]:.2%}')
        print(suggestion['details']['url'], suggestion['details']['common_names'])
        print()


# firstly create an identification
print('#' * 5, 'CREATE identification', '#' * 5)
response = requests.post(
    'https://plant.id/api/v3/identification',
    params={'details': 'url,common_names'},
    headers={'Api-Key': 'your_api_key'},
    json={'images': images},
)
#
identification = response.json()
print_identification(identification)

# Then create a conversation assigned to the identification
print('#' * 5, 'CREATE conversation', '#' * 5)
response = requests.post(
    f'https://plant.id/api/v3/identification/{identification["access_token"]}/conversation',
    headers={'Api-Key': 'your_api_key'},
    json={
        'question': 'Is this plant edible?',
        'prompt': 'You are an assistant for a plant identification app. Please answer the user\'s question.',
        'app_name': 'Plant.id',
        'model': 'gpt-3.5-turbo.demo',
    },
)
conversation = response.json()
print_conversation(conversation)

# You can assign a feedback(JSON) to a conversation
print('#' * 5, 'CREATE conversation feedback', '#' * 5)
requests.post(
    f'https://plant.id/api/v3/identification/{identification["access_token"]}/conversation/feedback',
    headers={'Api-Key': 'your_api_key'},
    json={
        'feedback': {'rating': 5},
    },
)


# Retrieve the conversation
print('#' * 5, 'GET conversation', '#' * 5)
response = requests.get(
    f'https://plant.id/api/v3/identification/{identification["access_token"]}/conversation',
    headers={'Api-Key': 'your_api_key'}
)
conversation = response.json()
print_conversation(conversation)


# Delete the identification
print('#' * 5, 'DELETE identification', '#' * 5)
requests.delete(
    f'https://plant.id/api/v3/identification/{identification["access_token"]}/conversation',
    headers={'Api-Key': 'your_api_key'}
)
