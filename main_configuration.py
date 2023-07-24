import tkinter

window = tkinter.Tk()
window.geometry("800x600")
# etiquet = tkinter.Label(window, text="aplication", bg="red")
# etiquet.pack(fill=tkinter.BOTH, expand=True)

button1 = tkinter.Button(window, text="aceptar", padx=30, pady=30)
button1.pack()

window.mainloop()
