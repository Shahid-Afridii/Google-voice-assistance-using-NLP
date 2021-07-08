'''pip install speechrecognition
pip install pyttsx3
pip install pyaudio
conda install -c anaconda portaudio'''

import pyaudio
import pyttsx3
import speech_recognition as sr

def NLP():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("'Listening Your voice'")
        r.pause_threshold = 0.9
        audio = r.listen(source)
        try:
            print("'Recognizing your voice'")
            user = r.recognize_google(audio)
            print("Converting your audio in to  text", user)
        except Exception as e:
            print (e)
            print("says it again")
            return "None"
    return user

def computer(com_audio):
    comp = pyttsx3.init()
    comp.say(com_audio)
    comp.runAndWait()


if __name__=='__main__':
    while True:
        commands = NLP()
        if "exit" in commands:
            computer("Thank You for using voice assitance")
            break
        if "what is python" in commands:
            computer("python is a programming language")
        if "what is insta" in commands:
            computer("insta is a social media")