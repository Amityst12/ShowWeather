import requests
import os
import sys
import json

def clear_terminal():
    #Clearing terminal
    os.system('cls' if os.name == 'nt' else 'clear')

key = "6900e3c518434df99dad2a8c5d0a3311"
baseURL = "http://api.openweathermap.org/data/2.5/forecast?id=293396&appid="
fullURL= baseURL + key


response = requests.get(fullURL)
data = response.json()

format = json.dumps(data, indent=4)

city = data["city"]["name"]
temp = data["list"][0]["main"]["temp"]
humidity = data["list"][0]["main"]["humidity"]
description = data["list"][0]["weather"][0]["description"]
wind_speed = data["list"][0]["wind"]["speed"]


clear_terminal
print(format)
print(f"City: {city} \nTemp: {temp} \nHumidity: {humidity}\nWind speed: {wind_speed} \n-{description}")