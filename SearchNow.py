import speech_recognition
import pyttsx3
import pywhatkit
import wikipedia
import webbrowser
def takeCommand():
    r = speech_recognition.Recognizer()
    with speech_recognition.Microphone() as source:
        print("Listening.....")
        r.pause_threshold = 1
        r.energy_threshold = 300
        audio = r.listen(source,0,4)
    try:
        print("Understanding..")
        query  = r.recognize_google(audio,language='en-in')
        print(f"You Said: {query}\n")
    except Exception as e:
        print("Say that again")
        return "None"
    return query

query = takeCommand().lower()


engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
engine.setProperty("rate",170)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    
def searchGoogle(query):
    if "google" in query:
        import wikipedia as googleScrap
        speak("This is what I found on the Google, sir.")
        
        try:
            query = query.replace("google", "")
            pywhatkit.search(query)
            result = googleScrap.summary(query, 1)
            speak(result)
            
        except:
            speak("Sorry, I am not able to find the information on the Google.")
            
            
            
def searchYoutube(query):
    if "youtube" in query:
        song = query.replace("play", "")
        song = query.replace("youtube", "")
        speak(f"Playing {song} on the Youtube.")
        pywhatkit.playonyt(song)
        web = "https://www.youtube.com/results?search_query=" + song
        webbrowser.open(web)
        pywhatkit.playonyt(song)
        speak("Done, Sir.")
        
def searchWikipedia(query):
    if "wikipedia" in query:
        speak("Searching Wikipedia...")
        query = query.replace("wikipedia", "")
        results = wikipedia.summary(query, sentences=1)
        speak("According to Wikipedia, ")
        print(results)
        speak(results)