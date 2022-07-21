import requests
import urllib
import os
import argparse
import dotenv
from additional_func import fetch_images
from pathlib import Path


def get_cli_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--image_count", default=10)
    return parser.parse_args()


def fetch_apod_images(dir_name, payload, url):
    response = requests.get(url, params=payload)
    response.raise_for_status()
    for json_element in response.json():
        try:
            apod_image_link = json_element['hdurl']
            file_path = urllib.parse.urlparse(apod_image_link).path
            _, file_name = os.path.split(file_path)
            file_save_path = Path(dir_name, file_name)
            fetch_images(apod_image_link, file_save_path)
        except KeyError:
            pass


if __name__ == '__main__':
    dotenv.load_dotenv()
    NASA_TOKEN = os.getenv("NASA_TOKEN")
    image_count = get_cli_args().image_count
    dir_name = Path('images', 'apod_images')
    os.makedirs(dir_name, exist_ok=True)
    url = "https://api.nasa.gov/planetary/apod"
    payload = {
        'api_key': '{}'.format(NASA_TOKEN),
        'count': '{}'.format(image_count)
    }
    try:
        fetch_apod_images(dir_name, payload, url)
    except(requests.HTTPError, requests.ConnectionError):
        print('Не удалось получить данные с сервера')
