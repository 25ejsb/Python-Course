from tkinter import *
import requests

response = requests.get("https://api.kanye.rest/")
json = response.json()["quote"]

window = Tk()
window.title("Cool Quotes")
window.minsize(500, 500)
window.maxsize(500, 500)

canvas = Canvas(width=400, height=500, highlightthickness=0)
photo = PhotoImage(file="Day33/background.png")
canvas.create_image(250, 250, image=photo)
newText = canvas.create_text(220, 230, text=str(json), font=("Arial", 20, "bold"), fill="white", width=250)
canvas.grid(column=0, row=0)

window.mainloop()