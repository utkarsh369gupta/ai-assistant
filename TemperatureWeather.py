import os
from dotenv import load_dotenv
import requests

load_dotenv()

api_key = os.getenv('OPENWEATHER_API_KEY')
def get_temperature(city):
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    
    complete_url = f"{base_url}q={city}&appid={api_key}&units=metric"
    
    response = requests.get(complete_url)
    
    if response.status_code == 200:
        data = response.json()
        temperature = data['main']['temp']
        return temperature
    else:
        return None
    
def get_weather(city):
     
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    
    complete_url = f"{base_url}q={city}&appid={api_key}&units=metric"
    
    response = requests.get(complete_url)
    
    if response.status_code == 200:
        data = response.json()
        weather = data['weather']
        wea = weather[0]['description']
        return wea
    else:
        return None
