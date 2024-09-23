import pyttsx3 as p 
import speech_recognition as sr
import datetime
import webbrowser


engine = p.init("sapi5")
voice = engine.getProperty('voices')
engine.setProperty('voice',voice[0].id)
engine.setProperty('rate',200)
engine.setProperty('volume',1.0)
engine.say("hello")
engine.runAndWait
def speakaudio(audio):
    engine.say(audio)
    engine.runAndWait()
from assistantfunctions import time
time()
engine.say(time())
engine.runAndWait
def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:  
        print("Listening...")
        r.adjust_for_ambient_noise(source)  
        r.pause_threshold = 1
        r.energy_threshold = 300
        audio = r.listen(source, timeout=5) 

    try:
        print("Recognizing...")
        query = r.recognize_google_cloud(audio, language='en-in') 
        print(f"User said: {query}\n")
    except Exception as e:
        print("Say that again...")
        return "None" 
    return query

if __name__ == "__main__":
    print("Taking commands...")
    
    while True:
        query = takecommand().lower()  
        from assistantfunctions import time
        time()
        if "go to sleep" in query:
            speakaudio("Closing the program. You can wake me up by saying wake up.")
            break
        elif "hello" in query:
            speakaudio("Hello, sir! How can I assist you?")
        elif "fine" in query:
            speakaudio("That's good, sir. How can I assist you?")
        elif "time now" in query:
            from assistantfunctions import tell_time 
            tell_time()
        else:
            continue
        