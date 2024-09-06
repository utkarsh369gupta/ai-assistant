import pyttsx3  # this is a text-to-speech conversion library in Python.
# this is a speech recognition library in Python.
import speech_recognition as sr
import requests
from bs4 import BeautifulSoup
import datetime
from time import sleep


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
engine.setProperty('rate', 200)  # Speed of speech


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


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

                elif "open" in query:
                    from Dictapp import openappweb
                    openappweb(query)
                elif "close" in query:
                    from Dictapp import closeappweb
                    closeappweb(query)

                elif "google" in query:
                    from SearchNow import searchGoogle
                    searchGoogle(query)
                elif "youtube" in query:
                    from SearchNow import searchYoutube
                    searchYoutube(query)
                elif "wikipedia" in query:
                    from SearchNow import searchWikipedia
                    searchWikipedia(query)

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

                elif 'exit' in query:
                    speak(
                        "Your desktop assistant is shutting down. Good bye! Have a nice day, sir.")
                    break
