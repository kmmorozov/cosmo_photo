import requests
import argparse
from additional_func import fetch_images
from additional_func import create_file_path
from pathlib import Path


def get_cli_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--launch_number", default=100)
    return parser.parse_args()


def fetch_spacex_last_launch(dir_name):
    response = requests.get(url, headers=headers, data=payload)
    response.raise_for_status()
    photo_links = response.json()['links']['flickr_images']
    for spaceX_image_link in photo_links:
        file_save_path = create_file_path(spaceX_image_link, dir_name)
        fetch_images(spaceX_image_link, file_save_path)
    return True


if __name__ == '__main__':
    launch_number = get_cli_args().launch_number
    url = "https://api.spacexdata.com/v3/launches/{}".format(launch_number)
    payload = {'filter': 'links,flickr_images'}
    headers = {}
    dir_name = Path('images', 'spacex_images')
    Path(dir_name).mkdir(exist_ok=True)
    try:
        fetch_spacex_last_launch(dir_name)
    except requests.HTTPError as e:
        print('Ошибка HTTP: {}'.format(e))
    except requests.ConnectionError as e:
        print('Ошибка подключения: {}'.format(e))
