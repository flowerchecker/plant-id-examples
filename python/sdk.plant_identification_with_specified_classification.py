from kindwise import PlantApi

# classification_level - str (optional) - classification model can give plant identification at 3 levels of taxonomy: genus, species and infraspecies (includes cultivars, subspecies, varieties and trademarks).
# This attribute allows to adjust which type of taxon is presented in response.
#
# species - default - suggested plants are genus and species
# all - suggested plants are genus, species and infraspecies
# genus - suggested plants are only genus

classification_level = 'genus'
api = PlantApi('your_api_key')
identification = api.identify(
    '../images/unknown_plant.jpg',
    details=['url', 'common_names'],
    classification_level=classification_level
)

print('is plant' if identification.result.is_plant.binary else 'is not plant')
for suggestion in identification.result.classification.suggestions:
    print(suggestion.name)
    print(f'probability {suggestion.probability:.2%}')
    print(suggestion.details['url'], suggestion.details['common_names'])
    print()


# classification_raw - bool (optional) - if true, suggestions of classification are kept in 3 original taxonomy levels (genus, species and infraspecies), without postprocessing.
# Please note that the response structure is changed, see the example:
# https://www.postman.com/winter-shadow-932363/workspace/kindwise/example/24599534-7ea4e714-093e-4f0b-b435-58dcbe587f0b

identification = api.identify(
    '../images/unknown_plant.jpg',
    details=['url', 'common_names'],
    classification_raw=True)

suggestions = identification.result.classification.suggestions
suggestion_list = []

for suggestion in [suggestions.genus, suggestions.species, suggestions.infraspecies]:
    if suggestion:
        suggestion_list.append(suggestion[0])

for suggestion in suggestion_list:
    print(suggestion.name)
    print(f'probability {suggestion.probability:.2%}')
    print(suggestion.details['url'], suggestion.details['common_names'])
    print()