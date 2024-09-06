import os 
import pyautogui
import webbrowser
import pyttsx3

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
engine.setProperty('rate', 200)  # Speed of speech


def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    
dictapp = {"commandprompt":"cmd","paint":"paint","word":"winword","excel":"excel","chrome":"chrome","vscode":"code","powerpoint":"powerpnt"}

def openappweb(query):
    speak("Launching, sir")
    if ".com" in query or ".co.in" in query or ".org" in query:
        query = query.replace("open","")
        query = query.replace("jarvis","")
        query = query.replace("launch","")
        query = query.replace(" ","")
        webbrowser.open(f"https://www.{query}")
    else:
        keys = list(dictapp.keys())
        for app in keys:
            if app in query:
                os.system(f"start {dictapp[app]}")
                
def closeappweb(query):
    speak("Closing, sir")
    
    # Closing browser tabs
    tab_count = 0
    if "one tab" in query or "1 tab" in query:
        tab_count = 1
    elif "2 tab" in query:
        tab_count = 2
    elif "3 tab" in query:
        tab_count = 3
    elif "4 tab" in query:
        tab_count = 4
    elif "5 tab" in query:
        tab_count = 5
    
    for _ in range(tab_count):
        pyautogui.hotkey("ctrl", "w")
        sleep(0.5)
    
    if tab_count > 0:
        speak("All tabs closed")
        return  

    else:
        keys = list(dictapp.keys())
        for app in keys:
            if app in query:
                os.system(f"taskkill /f /im {dictapp[app]}.exe")