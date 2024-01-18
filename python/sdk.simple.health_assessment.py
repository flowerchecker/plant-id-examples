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
