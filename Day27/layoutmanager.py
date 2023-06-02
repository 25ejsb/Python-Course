from tkinter import *
window = Tk()
window.title("My First Program")
window.minsize(width=500, height=300)

my_label = Label(text="I Am a Label", font=("Arial", 24, "bold"))
my_label.config(text="New Text")
my_label.grid(column=0, row=0)

button = Button(text="Click me")
button.grid(column=0, row=1)

input = Entry(width=10)
print(input.get())
input.place(x=100, y=100)

window.mainloop()