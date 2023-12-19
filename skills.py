import os
import webbrowser
import sys
import subprocess
from config import API_KEY

import voice

try:
    import requests  # pip install requests
except:
    pass


def browser():
    '''Открывает браузер заданнный по уполчанию в системе с url указанным здесь'''

    webbrowser.open('https://www.youtube.com', new=2)


def game():
    '''Нужно разместить путь к exe файлу любого вашего приложения'''
    try:
        subprocess.Popen('C:/Program Files/paint.net/PaintDotNet.exe')
    except:
        voice.speaker('Путь к файлу не найден, проверьте, правильный ли он')


def offpc():
    # Эта команда отключает ПК под управлением Windows

    # os.system('shutdown \s')
    print('пк был бы выключен, но команде # в коде мешает;)))')


def weather():
    '''Для работы этого кода нужно зарегистрироваться на сайте
    https://openweathermap.org или переделать на ваше усмотрение под что-то другое'''
    try:
        params = {'q': 'London', 'units': 'metric', 'lang': 'ru', 'appid': f'{API_KEY}'}
        response = requests.get(f'https://api.openweathermap.org/data/2.5/weather', params=params)
        if not response:
            raise
        w = response.json()
        voice.speaker(f"На улице {w['weather'][0]['description']} {round(w['main']['temp'])} градусов")

    except:
        voice.speaker('Произошла ошибка при попытке запроса к ресурсу API, проверь код')


def offBot():
    '''Отключает бота'''
    sys.exit()


def server():
    file_path = '/home/user/Desktop/Appium-linux-1.17.1.AppImage'
    subprocess.run(['chmod', '+x', file_path])  # Делаем файл исполняемым, если он еще не имеет прав на выполнение
    subprocess.Popen([file_path])  # Запускаем .AppImage файл


def passive():
    '''Функция заглушка при простом диалоге с ботом'''
    pass
