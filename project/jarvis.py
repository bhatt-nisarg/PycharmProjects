import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')

engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def WishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning! ")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon! ")
    else:
        speak("Good Evening! ")

    speak("I am Jarvis Sir. Please tell me how may I Help You")


def takeCommand():
    # it takes microphone input from the users and return string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        # r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)
        print("Say that again please...")
        return "None"
    return query
    # def sendEmail(to,content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server()
    server.login('youremail@gmail.com', 'your-password')
    server.sendmail('youremail@gmail.com', to, content)
    server.close()


if __name__ == "__main__":
    WishMe()
    while True:

        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak("Searchin Wekipedia...")
            query = query.replace("wikipedia", "")
            result = wikipedia.summary(query, sentences=2)
            print(result)
            speak(result)
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        elif 'open google' in query:
            webbrowser.open("google.com")
        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")
        # elif 'play music' in query:
        #     music_dir = 'music folder location'
        #     songs = os.listdir(music_dir)
        #     print(songs)
        #     os.startfile(os.path.join(music_dir,songs[0]))
        elif 'the time' in query:
            strTime = datetime.datetime.now().strtime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")
        # elif 'open vscode' in query:
        # codePath = "C:\Users\Nisarg\AppData\Local\Programs\Microsoft VS Code\Code.exe"
        # os.startfile(codePath)
        elif 'open android studio' in query:
            codePath = "C:\Program Files\Android\Android Studio\bin\studio64.exe"
            os.startfile(codePath)
        elif 'open pycharm' in query:
            codePath = "C:\Program Files\JetBrains\PyCharm Community Edition 2020.3\bin\pycharm64.exe"
            os.startfile(codePath)
            # elif 'email to me' in query:
        #     try:
        #         speak("What Should I say?")
        #         content = takeCommand()
        #         to = "bhattnisarg0@gmail.com"
        #         sendEmail(to, content)
        #         speak("Email has been sent!")
        #     except Exception as e:
        #         print(e)
        #         speak("email cant sent please try again")
