import speech_recognition as sr
import tkinter as tk
import docx as Document
import modules
import services

# app = tk.Tk()
# app.title('Asistente Data')
# app.geometry('120x80')

# modules.greeting()
while True:

    recognizer = sr.Recognizer()

    with sr.Microphone() as Micro:
        print('Escuchando')
        audio = recognizer.listen(Micro, phrase_time_limit=3)

    try:  # Si la aplicación entiende la petición, ejecutara los siguientes comandos:
        command = recognizer.recognize_google(audio, language="ES")
        print(f'Haz dicho "{command}"')

        if 'word' in command or 'abre word' in command or 'Abre Word' in command:
            modules.openWord()
        elif 'chrome' in command or 'abre chrome' in command or 'Abre Chrome' in command:
            modules.openChrome()
        elif 'cmd' in command or 'abre cmd' in command or 'Abre CMD' in command:
            modules.openCMD()
        elif 'data' in command or 'abre data' in command or 'Abre Data' in command:
            modules.openMaprex()

    except:  # En caso contrario, arrojara el siguiente mensaje:
        print('Lo siento, no pude entender tu petición, por favor vuelve a decir la petición')

# start = tk.Button(app, text='Iniciar', command=start())
# start.grid(row=0, column=0)

# app.mainloop()
