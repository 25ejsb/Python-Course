from turtle import Turtle

class Ball(Turtle):
    def __init__(self, direction, verticalang):
        super().__init__()
        self.penup()
        self.shapesize(stretch_wid=1, stretch_len=1)
        self.goto(0, 0)
        self.color("white")
        self.shape("circle")
        self.direction = direction
        self.verticalang = verticalang
        self.moving = False
        self.speed("fastest")

    def move(self):
        vertical = 0
        horizontal = 0
        if self.direction == "left":
            horizontal = -10
        else:
            horizontal = 10
        if self.verticalang == "up":
            vertical = 10
        else:
            vertical = -10
        self.goto(self.xcor()+horizontal, self.ycor()+vertical)
