import pyttsx3  # this is a text-to-speech conversion library in Python.
import speech_recognition as sr
import requests
from bs4 import BeautifulSoup
import datetime
from time import sleep
import os
import pyautogui
import random
import webbrowser


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
engine.setProperty('rate', 200)  # Speed of speech


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def alarm(query):
    timehere = open("Alarmtext.txt", "a")
    timehere.write(query)
    timehere.close()
    os.startfile("alarm.py")


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        r.energy_threshold = 300
        audio = r.listen(source, 0, 2)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"You said: {query}\n")

    except Exception as e:
        print("Say that again please...")
        return "None"
    return query


if __name__ == "__main__":
    # speak("Hello sir, your updated desktop assistant is in process. wake me up whenever you want me to assist you, sir?")
    while True:
        query = takeCommand().lower()
        if 'wake up' in query:
            from GreetMe import greetMe
            greetMe()

            while True:
                query = takeCommand().lower()
                if 'go to sleep' in query:
                    speak("Good bye! Have a nice day, sir.")
                    break

                elif "hello" in query:
                    speak("Hello sir, How can I help you?")
                elif "i am fine" in query:
                    speak("That's great sir. How can I help you?")
                elif "how are you" in query:
                    speak("I am fine sir.Everything is under your control.")
                elif "thank you" in query:
                    speak("You're welcome sir. How can I help you?")

                elif "pause" in query:
                    pyautogui.press("space")
                    speak("Paused, Sir")
                elif "play" in query:
                    pyautogui.press("space")
                    speak("Playing, Sir")
                elif "mute" in query:
                    pyautogui.press("m")
                    speak("Muted, Sir")

                elif "volume up" in query:
                    from keyboard import volumeup
                    speak("Turning volume up, sir")
                    volumeup()
                elif "volume down" in query:
                    from keyboard import volumedown
                    speak("Turning volume down, sir")
                    volumedown()

                elif "open" in query:
                    from Dictapp import openappweb
                    openappweb(query)
                elif "close" in query:
                    from Dictapp import closeappweb
                    closeappweb(query)

                elif "set an alarm" in query:
                    print("input time example:- 10 and 10 and 10")
                    speak("Set the time")
                    a = input("Please tell the time :- ")
                    alarm(a)
                    speak("Done,sir")

                elif "google" in query:
                    from SearchNow import searchGoogle
                    searchGoogle(query)
                elif "youtube" in query:
                    from SearchNow import searchYoutube
                    searchYoutube(query)
                elif "wikipedia" in query:
                    from SearchNow import searchWikipedia
                    searchWikipedia(query)
                    
                elif "news" in query:
                    from News import latestnews
                    latestnews()
                    
                elif "calculate" in query:
                    from Calculatenumbers import WolfRamAlpha
                    from Calculatenumbers import Calc
                    query = query.replace("calculate","")
                    query = query.replace("jarvis","")
                    Calc(query)
                    
                elif "whatsapp" in query:
                    from Whatsapp import sendMessage
                    sendMessage()
                    
                elif "temperature" in query:
                    from TemperatureWeather import get_temperature
                    city = query.split(" ")[-1].strip()
                    temp = get_temperature(city)
                    if temp:
                        speak(f"The current temperature in {
                              city} is {temp} degrees Celsius.")
                    else:
                        speak(f"Sorry, I couldn't retrieve the temperature for {
                              city} at the moment.")

                elif "weather" in query:
                    from TemperatureWeather import get_weather
                    city = query.split(" ")[-1].strip()
                    weather = get_weather(city)
                    if weather:
                        speak(f"The current weather in {city} is {weather} .")
                    else:
                        speak(f"Sorry, I couldn't retrieve the weather for {
                              city} at the moment.")

                elif "time" in query:
                    strTime = datetime.datetime.now().strftime("%H:%M")
                    speak(f"Sir, the time is {strTime}")
                    
                elif "remember that" in query:
                    rememberMessage = query.replace("remember that","")
                    rememberMessage = query.replace("jarvis","")
                    speak("You told me "+rememberMessage)
                    remember = open("Remember.txt","a")
                    remember.write(rememberMessage)
                    remember.close()
                    
                elif "what do you remember" in query:
                    remember = open("Remember.txt","r")
                    speak("You told me " + remember.read())
                    
                elif "tired" in query:
                    speak("Playing your favourite songs, sir")
                    a = (1,2,3)
                    b = random.choice(a)
                    if b==1:
                        webbrowser.open("https://www.youtube.com/watch?v=mY9fNwGE7YA")
                    elif b==2:
                        webbrowser.open("https://www.youtube.com/watch?v=ZAp3xJ7GsY8")
                    else:
                        webbrowser.open("https://www.youtube.com/watch?v=b-_hHBcSQtc")

                elif 'exit' in query:
                    speak(
                        "Your desktop assistant is shutting down. Good bye! Have a nice day, sir.")
                    break
