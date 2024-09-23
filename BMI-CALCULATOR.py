import speech_recognition as sr
import pyttsx3
import threading

# Text to Speech engine initialize karein
engine = pyttsx3.init()
engine.setProperty('rate', 150)

def speak(text):
    engine.say(text)
    engine.runAndWait()

# Speech recognition function
def take_command():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        while True:
            print("Listening...")
            recognizer.adjust_for_ambient_noise(source)
            try:
                audio = recognizer.listen(source, timeout=5)
                command = recognizer.recognize_google(audio, language='en-in')
                print(f"Recognized: {command}")
                if command.lower() == "exit":
                    speak("Goodbye!")
                    break
                else:
                    speak(f"You said: {command}")
            except sr.UnknownValueError:
                print("Could not understand the audio.")
            except sr.RequestError:
                print("Could not request results from Google Speech Recognition service.")

# Function to get text input from user
def get_text_input():
    while True:
        command = input("Please type your command (type 'exit' to stop): ")
        if command.lower() == "exit":
            speak("Goodbye!")
            break
        else:
            speak(f"You typed: {command}")

# Main function
def main():
    # Create threads for listening and writing
    listening_thread = threading.Thread(target=take_command)
    writing_thread = threading.Thread(target=get_text_input)

    listening_thread.start()
    writing_thread.start()

    # Wait for both threads to complete
    listening_thread.join()
    writing_thread.join()

if __name__ == "__main__":
    main()
