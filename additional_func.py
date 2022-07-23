import requests
import telegram
from datetime import datetime
import urllib
import os
from pathlib import Path


def write_file(save_path, content):
    with open(save_path, 'wb') as file:
        file.write(content)


def fetch_images(link, save_path):
    response = requests.get(link)
    response.raise_for_status()
    write_file(save_path, response.content)


def send_photo_to_channel(token, chat_id, file_path):
    bot = telegram.Bot(token=token)
    with open(file_path, 'rb') as file:
        bot.send_document(chat_id=chat_id, document=file)


def create_file_path(image_link, dir_name):
    file_path = urllib.parse.urlparse(image_link).path
    time_stamp = datetime.now().strftime('%Y%m%d%H%M%S')
    _, file_name = os.path.split(file_path)
    file_name = f'{time_stamp}{file_name}'
    file_save_path = Path(dir_name, file_name)
    return file_save_path
