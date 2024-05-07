import base64
import logging
import time

import requests


# Calling from remote server can increase the time taken to make the identification
# due to time needed to establish a connection (e.g. TLS handshake).
# You can speed up identification by establishing a connection before making the request and sharing the connection.


def make_identification(session=None):
    start_time = time.time()
    if session is None:
        post = requests.post
    else:
        post = session.post
    response = post(
        'https://plant.id/api/v3/identification',
        headers={'Api-Key': 'your_api_key'},
        json={'images': images},
    )
    end_time = time.time()
    assert response.status_code < 300, response.text
    print(f'Identification took {end_time - start_time:.2f} seconds')


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    with open('../images/unknown_plant.jpg', 'rb') as file:
        images = [base64.b64encode(file.read()).decode('ascii')]

    # Try without opened connection
    make_identification()  # Identification took 1.57 seconds

    session = requests.Session()
    session.get('https://plant.id/ping')  # pre-open connection
    time.sleep(1)
    # make identification when needed
    make_identification(session)  # Identification took 0.99 seconds
    make_identification(session)  # Identification took 0.51 seconds
    make_identification(session)  # Identification took 0.51 seconds
