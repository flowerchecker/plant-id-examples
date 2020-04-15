import base64
import requests
from time import sleep


key = "-- ask for one: https://forms.gle/yK1AY53YkYJjsc8X8 --"


def encode_files(file_names):
    files_encoded = []
    for file_name in file_names:
        with open(file_name, "rb") as file:
            files_encoded.append(base64.b64encode(file.read()).decode("ascii"))
    return files_encoded


def identify_plant(file_names):
    images = encode_files(file_names)

    params = {
        "api_key": key,
        "images": images,
        "latitude": 49.1951239,
        "longitude": 16.6077111,
        "datetime": 1582830233,
        "modifiers": ["crops_fast", "similar_images"],
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
        "plant_details": ["common_names",
                          "url",
                          "name_authority,",
                          "wiki_description",
                          "taxonomy",
                          "synonyms"],
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
    print(identify_plant(["photo1.jpg", "photo2.jpg"]))
