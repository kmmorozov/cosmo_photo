import telegram
import os
import random
from dotenv import load_dotenv
import argparse
from time import sleep
from additional_func import send_photo_to_channel


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--freq", default=14400)
    parser.add_argument("--dir", default='images')
    return parser.parse_args()


def get_file_paths_from_directory(directory):
    all_file_paths = list()
    for address, _, files in os.walk(directory):
        for name in files:
            file_path = os.path.join(address, name)
            all_file_paths.append(file_path)
    return all_file_paths


if __name__ == '__main__':
    load_dotenv()
    chat_id = os.getenv("TELEGRAM_CHAT_ID")
    token = os.getenv("TELEGRAM_TOKEN")
    time_out = get_args().freq
    directory = get_args().dir
    file_paths = get_file_paths_from_directory(directory)
    try:
        while True:
            for file_path in file_paths:
                send_photo_to_channel(token, chat_id, file_path)
                sleep(int(time_out))
            random.shuffle(file_path)
    except telegram.error.NetworkError as e:
        print('Ошибка подключения: {}'.format(e))
    except telegram.error.InvalidToken as e:
        print('Вы ввели неверный токен: {}.'.format(e))
