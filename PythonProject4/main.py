from speech_module import listen, speak
from task_module import get_weather

def handle_command(command):
    if "weather" in command:
        speak("Which city?")
        city = listen()
        weather_info = get_weather(city)
        speak(weather_info)
    elif "hello" in command:
        speak("Hello! I'm your assistant!")
    elif "stop" in command or "bye" in command:
        speak("Bye")
        exit()
    else:
        speak("Sorry, I don't understand that yet!")

if __name__ == "__main__":
    speak("Hey! I am ready to help you. Speak now!")
    while True:
        command = listen()
        if command:
            handle_command(command)
