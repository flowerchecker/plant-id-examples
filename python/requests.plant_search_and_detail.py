import requests


# Search plant knowledge base by query. Plants are searchable by scientific names, common names (in specified
# language), synonyms. Plant name and query are always matched from start of a word., i.e. "Aloe vera" is searchable
# by "Aloe", "Alo", "Vera", "ver", "Aloe vera"...


plant_for_search = 'aloe vera'
limit = 3        # int (optional) - maximum of returned result, max. 20, default 10
language = 'de'  # two-letter ISO 639-1 language code (optional, default en) - language of common names can be
# multiple (up to 3), separated by comma - i.e. (en,de,sv)

response = requests.get(
    'https://plant.id/api/v3/kb/plants/name_search',
    params={'q': plant_for_search, 'limit': limit, 'lang': language},
    headers={'Api-Key': 'your_api_key'},
)

search = response.json()
print(search)   # {'entities': [{'matched_in': 'Aloe vera', 'matched_in_type': 'entity_name', 'access_token':
# 'RXE1Vxh5ZlYNOChOATB9TQ04CDh6Tgw0XWxQZ1FiVGU-', 'match_position': 0, 'match_length': 9, 'entity_name': 'Aloe
# vera'}, {'matched_in': 'Aloe vera', 'matched_in_type': 'synonym', 'access_token':
# 'E3FuV015NFYMOCpOCDB7TVo4Wjh6TgI0XGwBZ1BiXWU-', 'match_position': 0, 'match_length': 9, 'entity_name': 'Aloe
# succotrina'}, {'matched_in': 'Aloe vera var. officinalis', 'matched_in_type': 'synonym', 'access_token':
# 'EnExVxp5b1YAOHlOCDArTVw4CjgqTlE0XWxXZ1RiUmU-', 'match_position': 0, 'match_length': 9, 'entity_name': 'Aloe
# officinalis'}], 'entities_trimmed': False, 'limit': 3}


# Get entity details based on access token from Plant search endpoint.
# One call cost 0.5 credits.


access_token = search['entities'][0]['access_token']
requested_plant_details = ('common_names,url,description,taxonomy,rank,gbif_id,inaturalist_id,image,synonyms,'
                           'edible_parts,watering,propagation_methods')
# comma separated list of requested plant details (required) see detail description in documentation (
# https://plant.id/docs)

response = requests.get(
    f'https://plant.id/api/v3/kb/plants/{access_token}',
    params={'details': requested_plant_details, 'lang': language},
    headers={'Api-Key': 'your_api_key'},
)

detail = response.json()
print(detail)   # {'common_names': ['Echte Aloe'], 'taxonomy': {'class': 'Liliopsida', 'genus': 'Aloe', 'order':
# 'Asparagales', 'family': 'Asphodelaceae', 'phylum': 'Tracheophyta', 'kingdom': 'Plantae'},
# 'url': 'https://de.wikipedia.org/wiki/Echte_Aloe', 'gbif_id': 2777724, 'inaturalist_id': 126882, 'rank': 'species',
# 'description': {'value': 'Die Echte Aloe (Aloe vera) ist eine Pflanzenart aus der Gattung der Aloen (Aloe) in der
# Unterfamilie der Affodillgewächse (Asphodeloideae). Das Artepitheton vera ist lateinisch und bedeutet u. a.
# „wahr“.', 'citation': 'https://de.wikipedia.org/wiki/Echte_Aloe', 'license_name': 'CC BY-SA 3.0', 'license_url':
# 'https://creativecommons.org/licenses/by-sa/3.0/'}, 'synonyms': ['Aloe barbadensis', 'Aloe barbadensis subsp.
# chinensis', 'Aloe barbadensis var. chinensis', 'Aloe chinensis', 'Aloe elongata', 'Aloe flava', 'Aloe humilis',
# 'Aloe indica', 'Aloe lanzae', 'Aloe littoralis', 'Aloe maculata', 'Aloe perfoliata subsp. barbadensis',
# 'Aloe perfoliata subsp. vera', 'Aloe perfoliata var. barbadensis', 'Aloe perfoliata var. vera', 'Aloe rubescens',
# 'Aloe variegata', 'Aloe vera subsp. chinensis', 'Aloe vera subsp. lanzae', 'Aloe vera subsp. littoralis',
# 'Aloe vera var. chinensis', 'Aloe vera var. lanzae', 'Aloe vera var. littoralis', 'Aloe vulgaris'],
# 'image': {'value': 'https://plant-id.ams3.cdn.digitaloceanspaces.com/knowledge_base/wikidata/462
# /46200b659607cd7d6cf766db0a954391ac8d775d.jpg', 'citation': 'http://www.hear.org/starr/', 'license_name': 'CC BY
# 3.0', 'license_url': 'https://creativecommons.org/licenses/by/3.0/'}, 'edible_parts': ['seeds', 'leaves'],
# 'watering': {'max': 1, 'min': 1}, 'propagation_methods': ['division', 'seeds'], 'language': 'de', 'entity_id':
# '4ba05f1050481731', 'name': 'Aloe vera'}

