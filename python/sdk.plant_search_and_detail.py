from kindwise import PlantApi, SearchResult, PlantKBType


# Search plant knowledge base by query. Plants are searchable by scientific names, common names (in specified
# language), synonyms. Plant name and query are always matched from start of a word., i.e. "Aloe vera" is searchable
# by "Aloe", "Alo", "Vera", "ver", "Aloe vera"...


api = PlantApi('your_api_key')

plant_for_search = 'aloe vera'
kb_type = PlantKBType.PLANTS    # str (optional, default plants), also 'diseases' can be searched.
limit = 3        # int (optional) - maximum of returned result, max. 20, default 10
language = 'de'  # two-letter ISO 639-1 language code (optional, default en) - language of common names can be
# multiple (up to 3), separated by comma - i.e. (en,de,sv)
search_result: SearchResult = api.search(plant_for_search, language=language, limit=limit, kb_type=kb_type)

print(search_result)    # SearchResult(entities=[SearchEntity(matched_in='Aloe vera', matched_in_type='entity_name',
# access_token='dkIkRiNCCDh7TixKf04CMgUwZlYDN3FJAzIAN3hLeEk-', match_position=0, match_length=9), SearchEntity(
# matched_in='Aloe vera', matched_in_type='synonym', access_token='IEJ_RnZCWjh6Ti5Kdk4EMlIwNFYDN39JAjJRN3lLcUk-',
# match_position=0, match_length=9), SearchEntity(matched_in='Aloe vera var. officinalis', matched_in_type='synonym',
# access_token='IUIgRiFCATh2Tn1Kdk5UMlQwZFZTNyxJAzIHN31Lfkk-', match_position=0, match_length=9)],
# entities_trimmed=False, limit=3)


# Get entity details based on access token from Plant search endpoint.
# One call cost 0.5 credits.

access_token = search_result.entities[0].access_token
requested_plant_details = ('common_names,url,description,taxonomy,rank,gbif_id,inaturalist_id,image,synonyms,'
                           'edible_parts,watering,propagation_methods')
# comma separated list of requested plant details (required) see detail description in documentation (
# https://plant.id/docs)

entity_details = api.get_kb_detail(access_token, requested_plant_details, language=language, kb_type=kb_type)
# entity_details = api.get_kb_detail(access_token, requested_plant_details, kb_type=kb_type)
print(entity_details)   # {'common_names': ['Echte Aloe'], 'taxonomy': {'class': 'Liliopsida', 'genus': 'Aloe',
# 'order': 'Asparagales', 'family': 'Asphodelaceae', 'phylum': 'Tracheophyta', 'kingdom': 'Plantae'},
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
