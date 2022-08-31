import base64
import requests


def encode_file(file_name):
    with open(file_name, "rb") as file:
        return base64.b64encode(file.read()).decode("ascii")


def identify_plant(file_names):
    # More optional parameters: https://github.com/flowerchecker/Plant-id-API/wiki/Plant-Health-Assessment
    params = {
        "images": [encode_file(img) for img in file_names],
        "latitude": 49.1951239,
        "longitude": 16.6077111,
        "datetime": 1582830233,
        # Modifiers docs: https://github.com/flowerchecker/Plant-id-API/wiki/Modifiers
        "modifiers": ["crops_fast", "similar_images"],
        "language": "en",
        # Disease details docs: https://github.com/flowerchecker/Plant-id-API/wiki/Disease-details
        "disease_details": ["cause",
                          "common_names",
                          "classification",
                          "description",
                          "treatment",
                          "url",
                          ],
        }

    headers = {
        "Content-Type": "application/json",
        "Api-Key": "-- ask for one: https://web.plant.id/api-access-request/ --",
        }

    response = requests.post("https://api.plant.id/v2/health_assessment",
                             json=params,
                             headers=headers)

    return response.json()


if __name__ == '__main__':
    print(identify_plant(["../img/photo1.jpg", "../img/photo2.jpg", "../img/photo3.jpg"]))
