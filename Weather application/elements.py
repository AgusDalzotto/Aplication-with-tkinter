from tkinter import *
import requests
from main_program import *


def obtain_weather(city):
    Api_key = "2d5c3b2148ef400e33d0e6b5cf1336bc"
    URL = "https://api.openweathermap.org/data/2.5/weather"
    parameters = {"APPID": Api_key, "q": city, "units": "metric"}
    response = requests.get(URL, params=parameters)
    weather = response.json()

    return show_response(weather)


def show_response(weather):
    name_of_city = weather["name"]
    description = weather["weather"][0]["description"]
    temperature = weather["main"]["temp"]

    show_city["text"] = name_of_city
    show_description["text"] = description
    show_temperature["text"] = temperature
