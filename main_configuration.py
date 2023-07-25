from tkinter import *

# base configuration
window = Tk()
window.geometry("800x600")
window.title("Weather application")
# base configuration

# entry
text_entry = Entry(window, font=("Arial", 30, "normal"), justify="center")
text_entry.pack(padx=40, pady=40)
# entry

# button
obtain_information = Button(window, text="Obtener el clima")
obtain_information.pack()
# button

show_weather = Label(text="weather", font=("Courier", 40, "normal"))
show_weather.pack()


window.mainloop()
