from turtle import Turtle

class Player(Turtle):
    def __init__(self, moveSpeed, maxNumber):
        super().__init__()
        self.left(90)
        self.penup()
        self.color("black")
        self.speed("fastest")
        self.goto(0, -380)
        self.shape("turtle")
        self.moveSpeed = moveSpeed
        self.maxNumber = maxNumber
        self.number = 0

    
    def movePlayer(self):
        self.goto(0, self.ycor()+self.moveSpeed)

    def stopMoving(self):
        self.speed = 0