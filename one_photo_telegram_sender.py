import os
import random
from dotenv import load_dotenv
import argparse
from additional_func import send_photo_to_channel


def get_cli_args():
    parser = argparse.ArgumentParser()
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
    directory = get_cli_args().dir
    file_paths = get_file_paths_from_directory(directory)
    try:
        random.shuffle(file_paths)
        send_photo_to_channel(token, chat_id, file_paths[0])
    except (telegram.error.NetworkError, telegram.error.InvalidToken):
        print('Ошибка отправки сообщения')
