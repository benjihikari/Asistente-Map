import speech_recognition as sr
import pyttsx3 as voice
import tkinter as tk
import docx as Document
import os

#Configuración de voz del asistente
# talk = voice.init('sapi5')
# voices = talk.getProperty('voices')
# talk.setProperty('voice', voices[0].id)
# talk.setProperty('rate', 120)

# def say(text):
#     talk.say()
#     talk.runAndWait()

#Funciones de ejecución
def openWord():
    word_path = "C:\\Users\\Usuario\\AppData\\Roaming\\Microsoft\\Internet Explorer\\Quick Launch\\User Pinned\\StartMenu\\Microsoft Word 2010";
    os.startfile(word_path)
    print('Abriendo Word')

#Ejecución de Asistente
while True:
    recognizer = sr.Recognizer()

    with sr.Microphone() as Micro:
        print('Escuchando')
        audio = recognizer.listen(Micro, phrase_time_limit=3)

    try: # Si la aplicación entiende la petición, ejecutara los siguientes comandos:
        command = recognizer.recognize_google(audio, language="es-ES")
        print(f'Haz dicho "{command}"')

        if 'asistente' in command or 'computadora' in command or 'data' in command:

            if 'abrir word' in command or 'abre word' in command:
                openWord()
    except: # En caso contrario, arrojara el siguiente mensaje:
        print('Lo siento, no pude entender tu petición, por favor vuelve a decir la petición')