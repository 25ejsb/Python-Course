import colorgram
from turtle import *
from random import *
t = Turtle()
t.penup()
t.pensize(20)
t.setx(5)
t.speed(40)
t.sety(5)
y = 5
t.hideturtle()
colormode(255)
rgb_colors = []
colors = colorgram.extract('Day18/image.webp', 30)
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    new_color = [r, g, b]
    rgb_colors.append(new_color)

num = 0
for i in range(100):
    randNum = randint(0, (len(rgb_colors)-1))
    t.penup()
    t.forward(40)
    t.pendown()
    t.color(rgb_colors[randNum][0], rgb_colors[randNum][1], rgb_colors[randNum][2])
    t.forward(2)
    num += 1
    if num >= 10:
        y += 30
        t.penup()
        t.setx(5)
        t.sety(y)
        t.pendown()
        num = 0

s = Screen()
s.exitonclick()