import base64
from datetime import datetime
from pathlib import Path

import requests
from exif import Image
import csv

DIRECTORY = './images'
API_KEY = '... your_api_key ...'


def encode_file(file_path: Path) -> str:
    """Encode a file in base64 format."""

    with open(file_path, 'rb') as file:
        return base64.b64encode(file.read()).decode('ascii')


def extract_exif(file_path: Path):
    """Extract EXIF data from a file."""

    image = Image(file_path)
    if image.has_exif:
        dt = image.get('datetime_original', None)
        if dt:
            dt = datetime.strptime(dt, '%Y:%m:%d %H:%M:%S')
        latitude = image.get('gps_latitude', None)
        if latitude:
            latitude = sum(x / 60**n for n, x in enumerate(latitude))
        longitude = image.get('gps_longitude', None)
        if longitude:
            longitude = sum(x / 60**n for n, x in enumerate(longitude))
        return dt, longitude, latitude
    return None, None, None


def identify_from_file(file_path: Path, api_key: str) -> dict:
    """Get plant identification result from a file."""

    dt, longitude, latitude = extract_exif(file_path)
    params = {
        'images': [encode_file(file_path)],
        'datetime': int(dt.timestamp()) if dt else None,
        'longitude': longitude,
        'latitude': latitude,
    }

    headers = {
        'Content-Type': 'application/json',
        'Api-Key': api_key,
    }

    response = requests.post('https://api.plant.id/v2/identify', json=params, headers=headers)
    assert response.status_code < 300, response.text
    return response.json()


def process_dir(dir_path: Path, api_key: str):
    """Process a directory with images and save the results to a CSV file."""

    with (dir_path / 'plant_id_identification.csv').open('w') as f:
        writer = csv.writer(f, delimiter=',')
        writer.writerow(['file_name', 'date', 'latitude', 'longitude', 'plant_name', 'probability'])
        for file_path in sorted(dir_path.iterdir()):
            print('processing:', file_path)
            if file_path.is_file() and file_path.suffix in ['.jpg', '.jpeg', '.png']:
                result = identify_from_file(file_path, api_key)
                writer.writerow(
                    [
                        file_path.name,
                        result['meta_data']['datetime'],
                        result['meta_data']['latitude'],
                        result['meta_data']['longitude'],
                        result['suggestions'][0]['plant_name'],
                        result['suggestions'][0]['probability'],
                    ],
                )


if __name__ == '__main__':
    process_dir(Path(DIRECTORY), API_KEY)
