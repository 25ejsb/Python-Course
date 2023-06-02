from tkinter import *
from tkinter import messagebox
import random, pyperclip, json

characters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "!", "~", "`", "@", "#", "$", "%", "^", "&", "*", "(", ")", "_", "-", "=", "+", "/", "<", ">", "?"]

window = Tk()
window.title("Password Manager")
window.minsize(600, 600)
window.maxsize(600, 600)
window.config(padx=50, pady=50)

logo = PhotoImage(file="Day29/logo.png")
canvas = Canvas(width=200, height=224)
canvas.create_image(100, 112, image=logo)
canvas.grid(column=1, row=0)

websiteLabel = Label(text="Website:", font=("Arial", 10))
websiteLabel.grid(column=0, row=1)

websiteEntry = Entry(width=20)
websiteEntry.place(x=153, y=228)

def find_password():
    website = str.lower(websiteEntry.get())
    try:
        with open("Day29/passwords.json") as file:
            data = json.load(file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No Websites saved to the Data File")
    else:
        if website.lower() in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=data[website]["website"], message=f"Email: {email}\nPassword: {password}")
        else:
            messagebox.showinfo(title="Could Not Find", message=f"Could not find the info for the website {website}")
    

searchButton = Button(text="Search", font=("Arial", 8), width=14, command=find_password)
searchButton.place(x=350, y=228)

emailLabel = Label(text="Email/Username:", font=("Arial", 10))
emailLabel.grid(column=0, row=2)

emailEntry = Entry(width=40)
emailEntry.grid(column=1, row=2)

passwordLabel = Label(text="Password:", font=("Arial", 10))
passwordLabel.grid(column=0, row=3)

passwordEntry = Entry(width=20)
passwordEntry.place(x=153, y=278)

def createPassword(length=13):
    newMessage = [random.choice(characters) for character in range(length)]
    passwordEntry.delete(0, END)
    passwordEntry.insert(END, string="".join(newMessage))
    copy = messagebox.askokcancel(title="Copy Password", message="Would you like to copy this password to clipboard?")
    if copy:
        pyperclip.copy(text="".join(newMessage))

passwordButton = Button(text="Generate Password", font=("Arial", 8), command=createPassword)
passwordButton.place(x=350, y=278)

def newInfo():
    if websiteEntry.get() != "" and emailEntry.get() != "" and passwordEntry != "":
        is_ok = messagebox.askokcancel(title=websiteEntry.get(), message=f"These are the details entered: \nEmail: {emailEntry.get()}\nPassword: {passwordEntry.get()}\nIs is ok to save?")
        if is_ok:
            with open("Day29/passwords.json", mode="r") as file:
                new_data = {
                    str.lower(websiteEntry.get()): {
                        "website": websiteEntry.get(),
                        "email": emailEntry.get(),
                        "password": passwordEntry.get()
                    }
                }
                # read data
                data = json.load(file)
                # append data
                data.update(new_data)
                websiteEntry.delete(0, END)
                emailEntry.delete(0, END)
                passwordEntry.delete(0, END)
            with open("Day29/passwords.json", mode="w") as file:
                # write data
                json.dump(data, file, indent=4)
    else:
        messagebox.showinfo(title="Invalid", message="You have empty fields. Please fill them in.")
addButton = Button(text="Add", width=40, font=("Arial", 10), command=newInfo)
addButton.grid(column=1, row=4)

window.mainloop()