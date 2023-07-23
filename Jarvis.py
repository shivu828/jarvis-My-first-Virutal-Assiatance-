import speech_recognition as sr
import pyttsx3

engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()
def take_voice_input():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")
        recognizer.pause_threshold = 1
        audio = recognizer.listen(source)

    try:
        print("Recognizing...")
        query = recognizer.recognize_google(audio, language="en-in")
        print(f"User: {query}")
        return query.lower()
    except sr.UnknownValueError:
        print("Sorry, I didn't catch that.")
        return ""
    except sr.RequestError:
        print("Sorry, I'm currently unable to process your request.")
        return ""


def main():
    speak("Hello, I am Jarvis. How can I assist you today?")

    while True:
        query = take_voice_input()

        # Add your own logic for handling user queries here
        # For example, you can check if the user said specific keywords and respond accordingly.

        if "hello" in query:
            speak("Hello! How can I help?")
        elif "goodbye" in query:
            speak("Goodbye! Have a great day!")
            break
        else:
            speak("I'm sorry, I don't understand that command.")

if __name__ == "__main__":
    main()
