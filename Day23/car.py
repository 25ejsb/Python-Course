from turtle import Turtle
from random import *
import turtle
turtle.colormode(255)

class Car():
    def __init__(self, speed):
        self.cars = []
        self.speed = speed

    def createCar(self):
        newCar = Turtle("classic", 0, False)
        newCar.speed("fastest")
        newCar.color("white")
        newCar.penup()
        newCar.showturtle()
        newCar.goto(300, randint(-320, 320))
        newCar.left(90)
        newCar.shape("square")
        newCar.shapesize(stretch_wid=3, stretch_len=2)
        newCar.color(randint(0, 255), randint(0, 255), randint(0, 255))
        self.cars.append(newCar)