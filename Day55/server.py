from flask import Flask
import random
app = Flask(__name__)

randNum = random.randint(0, 9)

@app.route('/')
def main():
    return "<h1>Guess a number between 0 and 9</h1>" \
    "<img src='https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif' alt='Giph'>"

@app.route('/<int:number>')
def num(number):
    if number < randNum:
        return "<h1 style='color:red;'>Too Low</h1>" \
        "<img src='https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif' alt='Low'>"
    elif number > randNum:
        return "<h1 style='color:purple;'>Too High</h1>" \
        "<img src='https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif' alt='High'>"
    else:
        return "<h1 style='color:green;'>You Found Me!</h1>" \
        "<img src='https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif' alt='Guessed'>"

if __name__ == '__main__':
    app.run(debug=True)