import urllib.parse
import requests
import urllib.parse
import os
from write_file import write_file


def fetch_epic_photo(links, directory_name):
    for link in links:
        file_url_path = urllib.parse.urlparse(link).path
        _, file_name = os.path.split(file_url_path)
        try:
            response = requests.get(link)
            response.raise_for_status()
            content = response.content
        except(requests.HTTPError, requests.ConnectionError):
            quit('Не удалось получить данные с сервера')
        write_file(directory_name, file_name, content)


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
    directory_name = 'images/epic_images'
    os.makedirs(directory_name, exist_ok=True)
    try:
        links = get_epic_photo_links(url, headers, payload)
        fetch_epic_photo(links, directory_name)
    except(requests.HTTPError, requests.ConnectionError):
        quit('Не удалось получить данные с сервера')
