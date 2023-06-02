from turtle import *

timmy = Turtle()

num = 3
while num < 11:
    angle = 360/num
    for i in range(num):
        timmy.forward(70)
        timmy.right(angle)
    num += 1