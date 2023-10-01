from tkinter import *
from elements import *

# base configuration
window = Tk()
window.geometry("1280x720")
window.title("Weather application")
# base configuration

# entry
city_entry = Entry(window, font=("Courier", 40, "normal"), justify="center")
city_entry.pack(padx=40, pady=40)
# entry

# button
obtain_information = Button(window, text="Obtain the weather", font=(
    "Courier", 30, "normal"), command=lambda: obtainWeather(city_entry.get()))
obtain_information.pack()
# button

# return information
show_weather = Label(text="weather", font=("Courier", 40, "normal"))
show_weather.pack()
# return information

# tags
show_city = Label(text="city", font=("Courier", 40, "normal"))
show_city.pack()

show_temperature = Label(text="temperature", font=("Courier", 40, "normal"))
show_temperature.pack()

show_description = Label(text="weather", font=("Courier", 40, "normal"))
show_description.pack()
# tags

# background color
window.configure(bg='light blue')
# background color

window.mainloop()
