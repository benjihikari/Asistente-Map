import datetime as datetime
import decouple as config
import os

# USERNAME = config('USER')
USERNAME = 'Benjamin'

def greeting():
    hour = datetime.now().hour

    if (hour >= 6) and (hour <= 12):
        print(f'Buenos Día {USERNAME}')
        # services.say(f'Buenos Días {USERNAME}')
    elif (hour >= 12) and (hour <= 16):
        print(f'Buenas Tardes {USERNAME}')
        # services.say(f'Buenas Tardes {USERNAME}')
    elif (hour >= 16) and (hour <= 19):
        print(f'Buenas Tardes {USERNAME}')
        # services.say(f'Buenas Tardes {USERNAME}')

def openWord():
    word_path = "C:\\Users\\Usuario\\AppData\\Roaming\\Microsoft\\Internet Explorer\\Quick Launch\\User Pinned\\StartMenu\\Microsoft Word 2010"
    os.startfile(word_path)
    print('Abriendo Word')
    # services.say('Abriendo Microsoft Word')

def openChrome():
    chrome_path = "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
    os.startfile(chrome_path)
    print('Abriendo Google Chrome')
    # services.say('Abriendo Google Chrome')

def openCMD():
    os.system('start cmd')
    print('Abriendo Consola Terminal')
    # services.say('Abriendo Consola Terminal')

def openMaprex():
    # os.system('start cmd')
    print('Abriendo MaPrex')
    # services.say('Abriendo Consola Terminal')