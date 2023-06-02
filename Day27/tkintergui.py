# tkinter documentation https://docs.python.org/3/library/tk.html
import tkinter

window = tkinter.Tk()
window.title("My First GUI Program")
window.minsize(500, 300)
window.maxsize(700, 500)

# Labels
my_label = tkinter.Label(text="I am a label", font=("Arial", 24, "bold"))
my_label_2 = tkinter.Label(text="I am another label", font=("Arial", 24, "bold"))
# Makes label appear, goes to center with expand
my_label.pack(expand=True)
my_label_2.pack(side="left")

# Buttons

def button_click():
    newText = input.get()
    my_label.config(text=newText)

button = tkinter.Button(text="Click Me!", font=("Arial", 24, "bold"), command=button_click)
button.pack(side="right")

# Text Box
input = tkinter.Entry(width=10)
input.pack(expand=True)

window.mainloop()