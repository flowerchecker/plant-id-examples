from kindwise import PlantApi, MessageType

api = PlantApi('your_api_key')


def print_conversation(conversation):
    for message in conversation.messages:
        if message.type == MessageType.ANSWER:
            print(f'App: {message.content}')
        else:
            print(f'Client: {message.content}')
        print()
    print('Feedback:', conversation.feedback.get('rating'))


def print_identification(identification):
    print('is plant' if identification.result.is_plant.binary else 'is not plant')
    for suggestion in identification.result.classification.suggestions:
        print(suggestion.name)
        print(f'probability {suggestion.probability:.2%}')
        print(suggestion.details['url'], suggestion.details['common_names'])
        print()


# firstly create an identification
print('#' * 5, 'CREATE identification', '#' * 5)
identification = api.identify('../images/unknown_plant.jpg', details=['url', 'common_names'])
print_identification(identification)

# Then create a conversation assigned to the identification
print('#' * 5, 'CREATE conversation', '#' * 5)
conversation = api.ask_question(identification, 'Is this plant edible?')
print_conversation(conversation)

# You can assign a feedback(JSON) to a conversation
print('#' * 5, 'CREATE conversation feedback', '#' * 5)
api.conversation_feedback(identification, {'rating': 5})


# Retrieve the conversation
conversation = api.get_conversation(identification)
print('#' * 5, 'GET conversation', '#' * 5)
print_conversation(conversation)

# Delete the identification
print('#' * 5, 'DELETE identification', '#' * 5)
api.delete_conversation(identification)
