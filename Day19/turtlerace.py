from turtle import Turtle, Screen
import turtle
from random import *

turtle.colormode(255)
winner = ""

class Player():
    def __init__(self, color, speed, index, title):
        self.color = color
        self.speed = speed
        self.index = index
        self.title = title
        self.t = Turtle()
        self.t.shapesize(1.5)
        self.t.shape("turtle")
        self.t.color(self.color[0], self.color[1], self.color[2])
        self.t.penup()
        self.t.speed(4)
        self.t.setx(-400)
        self.t.sety(300 - (self.index*50))
        self.t.pendown()
    
    def moveTurtle(self):
        self.t.forward(self.speed)
        if self.t.pos()[0] >= 300:
            global winner
            winner = self.title
        
    


screen = Screen()
user_bot = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")

maxSpeed = 7

colors = [
    Player((255, 0, 0), randint(1, maxSpeed), 1, "red"), 
    Player((252, 173, 3), randint(1, maxSpeed), 2, "orange"), 
    Player((255, 255, 0), randint(1, maxSpeed), 3, "yellow"), 
    Player((0, 255, 0), randint(1, maxSpeed), 4, "green"),
    Player((0, 0, 255), randint(1, maxSpeed), 5, "blue"),
    Player((252, 3, 231), randint(1, maxSpeed), 6, "purple"),
    Player((255, 0, 255), randint(1, maxSpeed), 7, "pink")
]

while winner == "":
    for i in colors:
        i.moveTurtle()


print(f"Game Over! {winner} is the winner!")
if user_bot.lower() == winner:
    print("You guessed right! You win!")
else:
    print("You guessed wrong! You lose.")
