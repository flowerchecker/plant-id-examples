from kindwise import PlantApi

# suggestion_filter - str (optional) or dict (optional) in format {'classification': 'FILTER_NAME (filter examples
# below)'} Restricts the output of the model to specified list of classes (region or plant type) and adjusts the
# probabilities. The lists can be combined with logical operators and parentheses. The lists are available
# https://plant.id/suggestion_filters.
#
# Examples:
# Vegetables - 'vegetable'
# Houseplants and wild plants in Europe - 'houseplant OR continent__europe'
# Trees in Europe and North America - '(continent__northern_america OR continent__europe) AND tree'

suggestion_filter = '(continent__northern_america OR continent__australasia) AND Succulent'
api = PlantApi('your_api_key')
identification = api.identify(
    '../images/unknown_plant.jpg',
    details=['url', 'common_names'],
    extra_post_params={'suggestion_filter': suggestion_filter},
)

print('is plant' if identification.result.is_plant.binary else 'is not plant')
for suggestion in identification.result.classification.suggestions:
    print(suggestion.name)
    print(f'probability {suggestion.probability:.2%}')
    print(suggestion.details['url'], suggestion.details['common_names'])
    print()
