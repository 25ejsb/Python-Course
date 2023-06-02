from turtle import Turtle
class Paddle(Turtle):
    def __init__(self, paddleSide):
        super().__init__()
        self.penup()
        self.paddleSide = paddleSide
        self.shape("square")
        self.speed("fastest")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.color("white")
        self.moving = False
        self.movedir = None
        if self.paddleSide.lower() == "left":
            self.goto(-390, 0)
        else:
            self.goto(380, 0)

    def moveUp(self):
        self.moving = True
        self.movedir = "up"
    
    def moveDown(self):
        self.moving = True
        self.movedir = "down"
    
    def stopMoving(self):
        self.moving = False
        self.movedir = None