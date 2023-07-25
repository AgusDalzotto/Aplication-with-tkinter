from tkinter import *
import requests


def obtain_weather(city):
    Api_key = "2d5c3b2148ef400e33d0e6b5cf1336bc"
    URL = "https://api.openweathermap.org/data/2.5/weather"
    parameters = {"APPID": Api_key, "q": city, "units": "metric"}
    response = requests.get(URL, params=parameters)
    weather = response.json()


def show_response(weather):
    name_of_city = weather["name"]
    description_of_city = weather["weather"][0]["description"]
    temperature_of_the_city = weather["main"]["temp"]
