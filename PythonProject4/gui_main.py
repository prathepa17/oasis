import tkinter as tk
import threading
from speech_module import listen, speak
from task_module import get_weather

def start_listening_thread():
    threading.Thread(target=start_listening).start()

def start_listening():
    command = listen()
    if "weather" in command:
        speak("Which city?")
        city = listen()
        result = get_weather(city)
        speak(result)
        output_label.config(text=result)
    elif "hello" in command:
        msg = "Hello how are you! I’m your smart assistant!"
        speak(msg)
        output_label.config(text=msg)
    elif "bye" in command or "stop" in command:
        msg = "Bye your wellcome"
        speak(msg)
        root.destroy()
    else:
        msg = "Sorry, I don't understand that!"
        speak(msg)
        output_label.config(text=msg)

root = tk.Tk()
root.title("My Voice Assistant")
root.geometry("400x300")

mic_button = tk.Button(root, text="🎤 Speak", command=start_listening, font=("Arial", 23))
mic_button.pack(pady=20)

output_label = tk.Label(root, text="", wraplength=300, font=("Arial", 12))
output_label.pack(pady=20)

root.mainloop()
