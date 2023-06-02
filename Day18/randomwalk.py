from turtle import *
from random import *

t = Turtle()
colormode(255)
t.pensize(15)
t.hideturtle()

angles = [90, 180, 270,  360]

while True:
    t.color(randint(0, 255), randint(0, 255), randint(0, 255))
    begin_fill()
    t.forward(20)
    t.right(choice(angles))