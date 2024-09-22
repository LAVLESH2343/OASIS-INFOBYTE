import speech_recognition as sr
import pyttsx3

# Text-to-speech engine initialize karna
engine = pyttsx3.init()

# Function to make assistant speak
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Function to listen to user's voice
def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        # r.pause_threshold = 5000 # Short pause allowed
        audio = r.listen(source)

    try:
        print("Recognizing...")
        command = r.recognize_google(audio, language='en-in')  # Recognize in Hindi and English
        print(f"User said: {command}\n")
    except Exception as e:
        print("Could not understand, please say that again.")
        return "None"
    return command.lower()

# Main function
def voice_assistant():
    speak("Hello, I am your assistant. How can I help you?")
    
    while True:
        command = take_command()

        if 'hello' in command:
            speak("Hello! How are you?")
        elif 'what is your name' in command:
            speak("My name is Python Assistant.")
        elif 'time' in command:
            from datetime import datetime
            time_now = datetime.now().strftime("%H:%M:%S")
            speak(f"The current time is {time_now}")
        elif 'exit' in command or 'bye' in command:
            speak("Goodbye! Have a great day!")
            break
        else:
            speak("Sorry, I did not understand that.")

# Start the assistant
voice_assistant()
