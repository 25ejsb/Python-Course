from turtle import Turtle
from random import *

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("blue")
        self.speed("fastest")
        self.goto(randint(-200, 200), randint(-200, 200))
    def refresh(self):
        self.goto(randint(-200, 200), randint(-200, 200))