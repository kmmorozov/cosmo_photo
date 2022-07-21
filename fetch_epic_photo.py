import urllib.parse
import requests
import urllib.parse
import os
from additional_func import fetch_images
from pathlib import Path


def fetch_epic_photo(links, directory_name):
    for link in links:
        file_url_path = urllib.parse.urlparse(link).path
        _, file_name = os.path.split(file_url_path)
        file_save_pass = Path(directory_name, file_name)
        fetch_images(link, file_save_pass)


def get_epic_photo_links(url, headers, payload):
    response = requests.get(url, headers=headers, params=payload)
    response.raise_for_status()
    photo_descriptions = response.json()
    links = []
    for photo_description in photo_descriptions:
        image_id = str(photo_description['image'])
        day_id = str(photo_description['date'])
        day_id, _ = day_id.replace('-', '/').split(' ')
        link = f'https://epic.gsfc.nasa.gov/archive/natural/{day_id}/png/{image_id}.png'
        links.append(link)
    return links


if __name__ == '__main__':
    url = "https://epic.gsfc.nasa.gov/api/natural"
    payload = {}
    headers = {}
    directory_name = Path('images', 'epic_images')
    os.makedirs(directory_name, exist_ok=True)
    try:
        links = get_epic_photo_links(url, headers, payload)
        fetch_epic_photo(links, directory_name)
    except(requests.HTTPError, requests.ConnectionError):
        quit('Не удалось получить данные с сервера')
