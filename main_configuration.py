import tkinter

window = tkinter.Tk()
window.geometry("800x600")
etiquet = tkinter.Label(window, text="aplication", bg="red")
etiquet.pack(fill=tkinter.BOTH, expand=True)

window.mainloop()
