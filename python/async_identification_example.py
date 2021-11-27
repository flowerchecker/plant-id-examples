import base64
import requests
from time import sleep


key = "-- ask for one: https://web.plant.id/api-access-request/ --"


def encode_file(file_name):
    with open(file_name, "rb") as file:
        return base64.b64encode(file.read()).decode("ascii")


def identify_plant(file_names):
    params = {
        "api_key": key,
        "images": [encode_file(img) for img in file_names],
        "latitude": 49.1951239,
        "longitude": 16.6077111,
        "datetime": 1582830233,
        "modifiers": ["crops_fast", "similar_images", "health_all"],
        }

    headers = {
        "Content-Type": "application/json"
        }

    response = requests.post("https://api.plant.id/v2/enqueue_identification",
                             json=params,
                             headers=headers).json()

    return get_result(response["id"])


def get_result(identification_id):
    params = {
        "api_key": key,
        "plant_language": "en",
        # plant details info: https://github.com/flowerchecker/Plant-id-API/wiki/Plant-details
        "plant_details": ["common_names",
                          "edible_parts",
                          "gbif_id"
                          "name_authority",
                          "propagation_methods",
                          "synonyms",
                          "taxonomy",
                          "url",
                          "wiki_description",
                          "wiki_image",
                          ],
        }

    headers = {
        "Content-Type": "application/json"
        }

    endpoint = "https://api.plant.id/v2/get_identification_result/"

    while True:
        print("Waiting for suggestions...")
        sleep(5)
        response = requests.post(endpoint + str(identification_id),
                                 json=params,
                                 headers=headers).json()
        if response["suggestions"] is not None:
            return response


if __name__ == '__main__':
    print(identify_plant(["../img/photo1.jpg", "../img/photo2.jpg", "../img/photo3.jpg"]))
