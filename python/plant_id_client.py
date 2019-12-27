"""
The purpose of this code is to show how to work with plant.id API.
You'll find API documentation at https://plant.id/api
"""

import base64
import requests
from time import sleep


secret_access_key = "-- ask for one at business@plant.id --"


class SendForIdentificationError(Exception):
    def __init__(self, m):
        self.message = m

    def __str__(self):
        return self.message


def send_for_identification(file_names):
    files_encoded = []
    for file_name in file_names:
        with open(file_name, "rb") as file:
            files_encoded.append(base64.b64encode(file.read()).decode("ascii"))

    params = {
        "latitude": 49.194161,
        "longitude": 16.603017,
        "week": 23,
        "images": files_encoded,
        "key": secret_access_key,
        "parameters": ["crops_fast"]
        }

    # see the docs for more optional attributes
    # for example "custom_id" allows you to work with your custom identifiers
    headers = {
        "Content-Type": "application/json"
    }

    response = requests.post("https://plant.id/api/identify", json=params,
                             headers=headers)

    if response.status_code != 200:
        raise SendForIdentificationError(response.text)

    # this reference allows you to gather the identification result
    # (once it is ready)
    return response.json().get("id")


def get_suggestions(request_id):
    params = {
        "key": secret_access_key,
        "ids": [request_id]
    }
    headers = {
        "Content-Type": "application/json"
    }

    # To keep it simple, we are pooling the API waiting for the server
    # to finish the identification.
    # The better way would be to utilize "callback_url" parameter in /identify
    # call to tell our server to call your"s server endpoint once
    # the identification is done.
    while True:
        print("Waiting for suggestions...")
        sleep(5)
        resp = requests.post("https://plant.id/api/check_identifications",
                             json=params, headers=headers).json()
        if resp[0]["suggestions"]:
            return resp[0]["suggestions"]

# more photos of the same plant increase the accuracy
request_id = send_for_identification(["photo1.jpg", "photo2.jpg"])

# just listing the suggested plant names here (without the certainty values)
for suggestion in get_suggestions(request_id):
    print(suggestion["plant"]["name"])
