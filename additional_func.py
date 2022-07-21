import requests
import telegram


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
