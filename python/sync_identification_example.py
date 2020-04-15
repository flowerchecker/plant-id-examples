import base64
import requests


def encode_files(file_names):
    files_encoded = []
    for file_name in file_names:
        with open(file_name, "rb") as file:
            files_encoded.append(base64.b64encode(file.read()).decode("ascii"))
    return files_encoded


def identify_plant(file_names):
    images = encode_files(file_names)

    # see the docs for more optional attributes
    params = {
        "api_key": "-- ask for one: https://forms.gle/yK1AY53YkYJjsc8X8 --",
        "images": images,
        "modifiers": ["crops_fast", "similar_images"],
        "plant_language": "en",
        "plant_details": ["common_names",
                          "url",
                          "name_authority",
                          "wiki_description",
                          "taxonomy",
                          "synonyms"],
        }

    headers = {
        "Content-Type": "application/json"
        }

    response = requests.post("https://api.plant.id/v2/identify",
                             json=params,
                             headers=headers)

    return response.json()


if __name__ == '__main__':
    print(identify_plant(["photo1.jpg", "photo2.jpg"]))
