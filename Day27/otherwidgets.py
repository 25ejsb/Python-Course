from tkinter import *

window = Tk()
window.title("Widget Examples")
window.minsize(700, 700)
window.maxsize(700, 700)

newText = Label(text="This is new text", font=("Arial", 10, "bold"))
newText.pack()

newButton = Button(text="Click me", font=("Arial", 15), width=7, height=1)
newButton.pack()

newLabel = Entry(width=30)
newLabel.pack()
newLabel.insert(END, string="Some text to begin with")

newTextBox = Text(height=5, width=30)
newTextBox.focus()
newTextBox.insert(END, "Something to put in")
print(newTextBox.get("1.0", END))
newTextBox.pack()

def spinbox_used():
    print(spinbox.get())

spinbox = Spinbox(from_=0, to=10, width=5, command=spinbox_used)
spinbox.pack()

def scale_used(value):
    print(value)
scale = Scale(from_=0, to=100, command=scale_used)
scale.pack()


def checkbox_used():
    print(checked_state.get())

checked_state = IntVar()
checkbutton = Checkbutton(text="Is On?", variable=checked_state, command=checkbox_used)
checked_state.get()
checkbutton.pack()

def radio_used():
    print(radio_state.get())

radio_state = IntVar()
radioButton = Radiobutton(text="Option1", value=1, variable=radio_state, command=radio_used)
radioButton2 = Radiobutton(text="Option2", value=2, variable=radio_state, command=radio_used)
radioButton.pack()
radioButton2.pack()

def listbox_used(event):
    print(listbox.get(listbox.curselection()))

listbox = Listbox(height=4)
fruits = ["Apple", "Orange", "Banana", "Pear"]
for item in fruits:
    listbox.insert(fruits.index(item), item)
listbox.bind("<<ListboxSelect>>", listbox_used)
listbox.pack()
window.mainloop()