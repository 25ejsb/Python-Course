from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

def moveFowards():
    tim.forward(10)

def moveBackwards():
    tim.backward(10)

def turnLeft():
    tim.left(5)

def turnRight():
    tim.right(5)

screen.listen()
screen.onkeypress(key="w", fun=moveFowards)
screen.onkeypress(key="s", fun=moveBackwards)
screen.onkeypress(key="a", fun=turnLeft)
screen.onkeypress(key="d", fun=turnRight)
screen.exitonclick()