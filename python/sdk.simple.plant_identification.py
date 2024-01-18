from kindwise import PlantApi

api = PlantApi('your_api_key')
identification = api.identify('../images/unknown_plant.jpg', details=['url', 'common_names'])

print('is plant' if identification.result.is_plant.binary else 'is not plant')
for suggestion in identification.result.classification.suggestions:
    print(suggestion.name)
    print(f'probability {suggestion.probability:.2%}')
    print(suggestion.details['url'], suggestion.details['common_names'])
    print()
