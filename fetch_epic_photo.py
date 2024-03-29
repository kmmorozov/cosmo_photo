import requests
from additional_func import fetch_images
from additional_func import create_file_path
from pathlib import Path


def fetch_epic_photo(links, directory_name):
    for link in links:
        file_save_path = create_file_path(link, directory_name)
        fetch_images(link, file_save_path)


def get_epic_photo_links(url):
    response = requests.get(url)
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
    directory_name = Path('images', 'epic_images')
    Path(directory_name).mkdir(exist_ok=True, parents=True)
    try:
        links = get_epic_photo_links(url)
        fetch_epic_photo(links, directory_name)
    except requests.HTTPError as e:
        print('Ошибка HTTP: {}'.format(e))
    except requests.ConnectionError as e:
        print('Ошибка подключения: {}'.format(e))
