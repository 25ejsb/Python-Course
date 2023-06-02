from tkinter import *

window = Tk()
window.title("Grid Manager")
window.minsize(600, 500)
window.config(padx=100, pady=200)

label = Label(text="Label", font=("Arial", 20, "bold"))
label.grid(column=0, row=0)

button1 = Button(text="Button1", font=("Arial", 20, "bold"))
button1.grid(column=1, row=1)

button2 = Button(text="Button2", font=("Arial", 20, "bold"))
button2.grid(column=2, row=0)

entry = Entry(width=20)
entry.grid(column=3, row=2)

window.mainloop()