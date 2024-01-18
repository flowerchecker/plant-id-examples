from time import sleep

from kindwise import PlantApi

if __name__ == '__main__':
    api = PlantApi('your_api_key')
    identification = api.identify('../images/unknown_plant.jpg', asynchronous=True)

    print('Waiting for results...')
    while identification.result is None:
        sleep(1)
        identification = api.get_identification(identification.access_token)
    print(identification.result)
