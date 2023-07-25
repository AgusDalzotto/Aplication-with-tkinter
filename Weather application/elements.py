from tkinter import *
import requests


def obtain_weather(city):
    Api_key = "2d5c3b2148ef400e33d0e6b5cf1336bc"
    URL = "https://api.openweathermap.org/data/2.5/weather"
    parameters = {"APPID": Api_key, "q": city, "units": "metric"}
    response = requests.get(URL, params=parameters)
    weather = response.json()


def show_response(weather):
    name = weather["name"]
    description = weather["weather"][0]["description"]
    temperature = weather["main"]["temp"]

    name_of_city["text"] = name
