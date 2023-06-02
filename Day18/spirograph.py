from math import *
from turtle import *
from random import *

radius = 90

t = Turtle()
t.speed(200)
colormode(255)
t.hideturtle()

for i in range(80):
    t.circle(100)
    t.color(randint(0, 255), randint(0, 255), randint(0, 255))
    t.right(5)