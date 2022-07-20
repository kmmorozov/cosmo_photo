import requests
import urllib
import os
import argparse
from write_file import write_file
from datetime import datetime


def get_cli_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--launch_number", default=100)
    launch_number = parser.parse_args().launch_number
    return launch_number


def fetch_spacex_last_launch(dir_name):
    response = requests.get(url, headers=headers, data=payload)
    response.raise_for_status()
    photo_links = response.json()['links']['flickr_images']
    for spaceX_image_link in photo_links:
        response = requests.get(spaceX_image_link)
        file_path = urllib.parse.urlparse(spaceX_image_link).path
        time_stamp = datetime.now().strftime('%Y%m%d%H%M%S')
        _, file_name = os.path.split(file_path)
        file_name = time_stamp + file_name
        response.raise_for_status()
        write_file(dir_name, file_name, response.content)

    return True


if __name__ == '__main__':
    launch_number = get_cli_args()
    url = "https://api.spacexdata.com/v3/launches/{}".format(launch_number)
    payload = {'filter': 'links,flickr_images'}
    headers = {}
    dir_name = 'images/spacex_images'
    os.makedirs(dir_name, exist_ok=True)
    try:
        fetch_spacex_last_launch(dir_name)
    except(requests.HTTPError, requests.ConnectionError):
        print('Не удалось получить данные с сервера')
