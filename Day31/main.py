from tkinter import *
from random import *
import csv

BACKGROUND_COLOR = "#B1DDC6"

window = Tk()
window.title("Flash Cards")
window.minsize(900, 700)
window.maxsize(900, 700)
window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)

words = []

def resetCards():
    with open("Day31/french_words.csv") as file:
        reader = csv.reader(file)
        for word in reader:
            words.append({"french": word[0], "english": word[1]})

try:
    with open("Day31/words_to_learn.csv") as file:
        reader = csv.reader(file)
        for word in reader:
            words.append({"french": word[0], "english": word[1]})
except FileNotFoundError:
    resetCards()

def newWordsToLearn():
    with open("Day31/words_to_learn.csv", mode="w") as file:
        for word in words:
            file.writelines([word["french"] + "," + word["english"] + "\n"])

newWordsToLearn()

card_front = PhotoImage(file="Day31/images/card_front.png")
back_card = PhotoImage(file="Day31/images/card_back.png")
canvas = Canvas(width=800, height=526, highlightthickness=0)
newcard = canvas.create_image(400, 263, image=card_front)
language = canvas.create_text(400, 150, text="Title", font=("Arial", 40, "italic"))
word = canvas.create_text(400, 275, text="Word", font=("Arial", 50, "bold"))
canvas.config(bg=BACKGROUND_COLOR)
canvas.grid(row=0, column=0, columnspan=2)
# column span allows columns to spread
card = None
time = 0

def answer(newlanguage, newtime):
    global card
    if newtime == time:
        canvas.itemconfig(newcard, image=back_card)
        if newlanguage == "english":
            newlanguage = "french"
        else: 
            newlanguage = "english"
        canvas.itemconfig(word, text=card[newlanguage])
        canvas.itemconfig(language, text=newlanguage.capitalize())

def new_card():
    global card, time
    card = choice(words)
    newlanguage = choice(["english", "french"])
    time += 1
    canvas.itemconfig(newcard, image=card_front)
    canvas.itemconfig(word, text=card[newlanguage])
    canvas.itemconfig(language, text=newlanguage.capitalize())
    window.after(3000, answer, newlanguage, time)

def accept():
    words.pop(words.index(card))
    if len(words) == 0:
        resetCards()
    new_card()
    newWordsToLearn()

def decline():
    new_card()

x_image = PhotoImage(file="Day31/images/wrong.png")
decline = Button(image=x_image, highlightthickness=0, command=decline)
decline.grid(row=1, column=0)
r_image = PhotoImage(file="Day31/images/right.png")
right = Button(image=r_image, highlightthickness=0, command=accept)
right.grid(row=1, column=1)

new_card()

window.mainloop()