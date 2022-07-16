import telegram
import os
import random
from dotenv import load_dotenv
import argparse
from time import sleep


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--freq", default=14400)
    parser.add_argument("--dir", default='./images')
    freq = parser.parse_args().freq
    directory = parser.parse_args().dir
    return freq, directory


def get_file_paths_from_directory(directory):
    all_file_paths = list()
    for address, _, files in os.walk(directory):
        for name in files:
            file_path = os.path.join(address, name)
            all_file_paths.append(file_path)
    return all_file_paths


def send_photo_to_channel(token, chat_id, file_paths):
    bot = telegram.Bot(token=token)
    for file_path in file_paths:
        with open(file_path, 'rb') as file:
            bot.send_document(chat_id=chat_id, document=file)
        sleep(int(time_out))
    while True:
        random.shuffle(file_paths)
        for file_path in file_paths:
            with open(file_path, 'rb') as file:
                bot.send_document(chat_id=chat_id, document=file)
            sleep(int(time_out))


if __name__ == '__main__':
    load_dotenv()
    chat_id = os.getenv("TELEGRAM_CHAT_ID")
    token = os.getenv("TELEGRAM_TOKEN")
    time_out, directory = get_args()
    file_paths = get_file_paths_from_directory(directory)
    try:
        send_photo_to_channel(token, chat_id, file_paths)
    except (telegram.error.NetworkError, telegram.error.InvalidToken):
        print('Ошибка отправки сообщения')
