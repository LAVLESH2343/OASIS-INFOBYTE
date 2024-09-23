import pyttsx3  # Use pyttsx3 instead of pyttsx
import datetime 
# import speech_recognition as sr

# Initialize the TTS engine
engine = pyttsx3.init("sapi5")
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)  
engine.setProperty('rate', 200)  
engine.setProperty('volume', 1.0) 
def speak(text):
    engine.say(text)
    engine.runAndWait()


def time():
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour < 12:
        speak("Good morning!")
    elif 12 <= hour < 18:
        speak("Good afternoon!")
    else:
        speak("Good evening!")

    speak("how i can assist you")


def tell_time():
    now = datetime.datetime.now()  
    hour = now.strftime("%I")  
    minute = now.strftime("%M")  
    period = now.strftime("%p")  
   
    current_time = f"The time is {hour} {minute} {period}"
    speak(current_time) 


speak("Hello, I will tell you the current time.")
tell_time()



