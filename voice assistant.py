import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser
import wikipedia


engine = pyttsx3.init()

def speak(text):
    print(f"Assistant: {text}")
    engine.say(text)
    engine.runAndWait()

def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening... 🎤")
        audio = recognizer.listen(source)

    try:
        command = recognizer.recognize_google(audio)
        print(f"You said: {command}")
        return command.lower()
    except sr.UnknownValueError:
        speak("Sorry, I couldn't understand.")
        return ""
    except sr.RequestError:
        speak("Network error.")
        return ""

def process_command(command):
    if 'hello' in command:
        speak("Hi! I'm your voice assistant.")
    elif 'time' in command:
        time_now = datetime.datetime.now().strftime('%I:%M %p')
        speak(f"The time is {time_now}")
    elif 'date' in command:
        date_today = datetime.datetime.now().strftime('%B %d, %Y')
        speak(f"Today's date is {date_today}")
    elif 'day'in command:
        day_now = datetime.datetime.now().strftime('%A')
        speak(f"Today's day is {day_now}")
    elif 'news' in command:
        speak("opening latest sports news")
        webbrowser.open("https://sports.ndtv.com/latest22")
    elif 'bye' in command or 'exit' in command:
        speak("Goodbye ! See you soon.")
        exit()
    else:
        speak("Sorry, I don't understand that.")

speak("Voice Assistant ready. Say something!")

while True:
    user_command = listen()
    if user_command:
        process_command(user_command)