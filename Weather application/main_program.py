from tkinter import *
from elements import obtain_weather

# base configuration
window = Tk()
window.geometry("800x600")
window.title("Weather application")
# base configuration

# entry
city_entry = Entry(window, font=("Arial", 40, "normal"), justify="center")
city_entry.pack(padx=40, pady=40)
# entry

# button
obtain_information = Button(window, text="Obtain the weather", font=(
    "Arial", 30, "normal"), command=lambda: obtain_weather(city_entry.get()))
obtain_information.pack()
# button

# return information
show_weather = Label(text="weather", font=("Courier", 40, "normal"))
show_weather.pack()
# return information

show_city = Label(text="city", font=("Courier", 40, "normal"))
show_city.pack()

show_temperature = Label(text="temperature", font=("Courier", 40, "normal"))
show_temperature.pack()

show_description = Label(text="weather", font=("Courier", 40, "normal"))
show_description.pack()

window.configure(bg='light blue')

window.mainloop()
