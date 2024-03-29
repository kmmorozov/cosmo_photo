import requests
import os
import argparse
import dotenv
from additional_func import fetch_images
from additional_func import create_file_path
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
            file_save_path = create_file_path(apod_image_link, dir_name)
            fetch_images(apod_image_link, file_save_path)
        except KeyError:
            pass


if __name__ == '__main__':
    dotenv.load_dotenv()
    NASA_TOKEN = os.getenv("NASA_TOKEN")
    image_count = get_cli_args().image_count
    dir_name = Path('images', 'apod_images')
    Path(dir_name).mkdir(exist_ok=True, parents=True)
    url = "https://api.nasa.gov/planetary/apod"
    payload = {
        'api_key': '{}'.format(NASA_TOKEN),
        'count': '{}'.format(image_count)
    }
    try:
        fetch_apod_images(dir_name, payload, url)
    except requests.HTTPError as e:
        print('Ошибка HTTP: {}'.format(e))
    except requests.ConnectionError as e:
        print('Ошибка подключения: {}'.format(e))
