import pyttsx3
import webbrowser
import smtplib
import random
import speech_recognition as sr
import wikipedia
import datetime
import os
import sys

engine = pyttsx3.init('sapi5')

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[len(voices)-1 ].id)


def speak(audio):
    print('Computer: ' + audio)
    engine.say(audio)
    engine.runAndWait()


def greetMe():
    currentH = int(datetime.datetime.now().hour)
    if currentH >= 0 and currentH < 12:
        return 'Good Morning Sir!!'

    if currentH >= 12 and currentH < 18:
        return 'Good Afternoon Sir!!'

    if currentH >= 18 and currentH != 0:
        return 'Good Evening Sir!!'

os.system('color 2')
speak(greetMe() + ' I am your digital Personal Assistant LEZA !!')
speak('How i Can help you?')
os.system('color 4')


def myCommand():
    r = sr.Recognizer()
    print("Listening...")
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
    try:
        query = r.recognize_google(audio, language='en-in')
        print('User: ' + query + '\n')

    except sr.UnknownValueError:
        speak('Sorry sir! I didn\'t get that! Try typing the command!')
        query = str(input('Command: '))

    return query


if __name__ == '__main__':

    while True:

        query = myCommand()
        query = query.lower()

        if 'open youtube' in query:
            speak('okay')
            webbrowser.open('www.youtube.com')

        elif 'open google' in query:
            speak('okay')
            webbrowser.open('www.google.co.in')

        elif 'open gmail' in query:
            speak('okay')
            webbrowser.open('www.gmail.com')

        elif "what\'s up" in query or 'how are you' in query:
            stMsgs = ['Just doing my thing!', 'I am fine!', 'Nice!', 'I am nice and full of energy']
            speak(random.choice(stMsgs))

        elif 'email' in query:
            speak('Who is the recipient? ')
            recipient = myCommand()

            if 'me' in recipient:
                try:
                    speak('What should I say? ')
                    content = myCommand()

                    server = smtplib.SMTP('smtp.gmail.com', 587)
                    server.ehlo()
                    server.starttls()
                    server.login("Your_Username", 'Your_Password')
                    server.sendmail('Your_Username', "Recipient_Username", content)
                    server.close()
                    speak('Email sent!')

                except:
                    speak('Sorry Sir! I am unable to send your message at this moment!')


        elif 'nothing' in query or 'abort' in query or 'stop' in query:
            speak('okay')
            speak('Bye Sir, have a good day.')
            sys.exit()

        elif 'hello' in query:
            speak('Hello Sir')

        elif 'bye' in query:
            speak('Bye Sir, have a good day.')
            sys.exit()

        elif 'play music' in query:
            music_folder = r'C:\Users\Pardeep\Music'
            music = ['_g.mp3','_h.mp3','_i.mp3','_j.mp3','_paste_songs_title_here.mp3']
            random_music = str(music_folder+random.choice(music))
            os.system(random_music)

            speak('Okay, here is your music! Enjoy!')


        else:
            query = query
            speak('Searching...')
            try:
                results = wikipedia.summary(query, sentences=2)
                speak('Got it.')
                speak('WIKIPEDIA says - ')
                speak(results)
            except:
                webbrowser.open('www.google.com')

        speak('Next Command! Sir!')

