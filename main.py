import pyttsx3
import datetime
import speech_recognition as sr
import pyaudio
import os

os.environ["HTTPS_PROXY"]="username@127.0.0.1"


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[1].id)
engine.setProperty('voice',voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good morning sir..have a nice day")
    elif hour>=12 and hour<18:
        speak("Good afternoon sir   have a nice day")
    else:
        speak("good evening sir")
    speak("is there anything    i need to do right now")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshhold=1
        audio = r.listen(source)
    try:
        print("Recognizing")
        query = r.recognize_google(audio,language='en-in')
        #print(f"user said{query}\n")

    except Exception as e:
        print(e)
        print("say that again please...")
        return "none"
    return query



if  __name__ == "__main__":

    speak("hello jarvis sir... how may i help you")
    wishMe()
    takeCommand()


