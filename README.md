# Фотографии космоса

Проект состоит из шести скриптов:

- скрипт скачивания фото по api с сайта spaceX ```
  fetch_spacex_images.py ```.
- скрипт скачивания фото по api с сайта NASA ```fetch_apod_images.py```.
- скрипт скачивания фото по api с сайта NASA epic ```.
  fetch_epic_photo.py ```
- Скрипт однократной публикации фото в телеграм канале ```one_photo_telegram_sender.py```.
- Скрипт периодической публикации фото в телеграм канале ```telegram_sender.py```.
- Дополнительный скрипт для вызова повторяющихся функций ```additional_func.py```

### Как это работает:

- Скрипты для скачивания фото автоматически создают папку
  ```images``` и подпапки с именами сервисов ```apod_images, epic_images, spacex_images``` и скачивают туда фото с
  соответствующих сервисов.
- При использовании только скриптов публикации необходимо создать папку ```images``` и разместить там фото для
  публикации.

#### fetch_spacex_images.py :

- Качает фотографии запусков SpaceX
  ([пример фото](https://live.staticflickr.com/65535/50242057637_ea4f98d517_o.jpg))
  при запуске скрипта нужно ввести номер запуска Spacex, если номер запуска не указан, будут скачаны фотографии 100
  запуска.

#### fetch_apod_images.py :

- Качает фотографии с сайта NASA ([пример фото](https://apod.nasa.gov/apod/a)) при запуске нужно ввести количество
  скачиваемых фото.
  Для работы необходим токен от NASA api, который можно получить по [ссылке](https://api.nasa.gov).

#### fetch_epic_photo.py

- Скачивает последние фотографии Земли полученные от DSCOVR Earth Polychromatic Imaging
  Camera, ( [пример фото](https://api.nasa.gov/EPIC/archive/natural/2019/05/30/png/epic_1b_20190530011359.png?api_key=DEMO_KEY))
  .

#### one_photo_telegram_sender.py

- Публикует случайную фотографию из папки ```images``` или ее подпапок в телеграм канал.

#### telegram_sender.py

- Периодически публикует фотографии из папки ```images``` и ее подпапок в телеграм канал. При можно указать интервал
  публикации, если он не указан, то фото будут публиковаться раз в 4 часа.

### Установка.

- Скачайте код
- Python3 должен быть уже установлен.
  Затем используйте `pip` для установки зависимостей:

```
pip install -r requirements.txt
```

- Часть настроек проекта берётся из переменных окружения.
  Чтобы их определить, создайте файл `.env` в корневом каталоге программы и запишите туда необходимые
  вам данные в таком формате: `ПЕРЕМЕННАЯ=значение`.

Вам понадобятся три переменные:

- `NASA_TOKEN` - секретный ключ ([ссылка](https://api.nasa.gov)).
- `TELEGRAM_TOKEN` - секретный ключ телеграм бота.
- `TELEGRAM_CHAT_ID` - chat_id вашего телеграм канала.

#### Инструкция telegram:

- Создайте телеграм бота с помощью [BotFather](https://telegram.me/BotFather)".
- Запомните токен вашего бота.
- Запустите бота командой /start.
- Добавьте бота в администраторы вашего телеграм канала.
- Запомните chat_id канала.

#### Запуск кода.

Для запуска скачивания фото используются следующие команды:

```bash
python3 fetch_spacex_images.py --launch_number=16
```

где ` 16` - это номер запуска.

```bash
python3 fetch_apod_images.py --image_count=23
```

где `23` - это количество фотографий для скачивания.

```bash
python3 fetch_epic_photo.py
```

После запуска любого из скриптов скачивания, появится папка ```images```, в ней появятся подпапка с именем
соответствующего сервиса ```apod_images, epic_images, spacex_images``` , в которой будут фотографии.

Для публикации фото в телеграм канал с помощью бота используются следующие команды:

```bash
python3 one_photo_telegram_sender.py
```

```bash
python3 telegram_sender.py --freq=3600 --dir=/home/user1/photo
``` 

где `3600`  - это промежуток времени между публикациями, a `/home/user1/photo` - путь до папки с фотографиями.

После запуска любого из скриптов отправки в канал телеграм должны будут отправиться фотографии.

## Цели проекта

Код написан в учебных целях — это урок в курсе по Python и веб-разработке на сайте [Devman](https://dvmn.org).

