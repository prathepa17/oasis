import requests
from api_keys import OPENWEATHER_API

def get_weather(city="Chennai"):
    try:
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={OPENWEATHER_API}&units=metric"
        data = requests.get(url).json()
        temp = data['main']['temp']
        desc = data['weather'][0]['description']
        return f"The weather in {city} is {temp}°C with {desc}."
    except:
        return "Couldn't fetch weather info now."
