from datetime import datetime

from kindwise import PlantApi

if __name__ == '__main__':
    api = PlantApi('your_api_key')
    identification = api.identify(
        ['../images/photo1.jpg', '../images/photo2.jpg'],
        latitude_longitude=(13.3966042, 23.3150361),
        date_time=datetime(2021, 5, 18),
        details=[
            'url',
            'common_names',
            'edible_parts',
            'name_authority',
            'gbif_id',
            'inaturalist_id',
            'synonyms',
            'taxonomy',
            'description',
            'url',
        ],
        language='de',
        similar_images=True,
    )

    print('is plant' if identification.result.is_plant.binary else 'is not plant')
    for suggestion in identification.result.classification.suggestions:
        print(suggestion.name)
        print(f'probability {suggestion.probability:.2%}')
        print(suggestion.details)
        print(suggestion.similar_images)
        print()
