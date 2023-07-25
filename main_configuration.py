from tkinter import *

# base configuration
window = Tk()
window.geometry("800x600")
window.title("Weather application")
window.mainloop()
# base configuration


show_text = Entry(window, font=("Courier", 30, "normal"), justify="center")
show_text.pack(padx=40, pady=40)

obtain_information = Button(window, text="Obtener el clima")
obtain_information.pack()

show_weather = Label(text="weather", font=("Courier", 40, "normal"))
show_weather.pack()
