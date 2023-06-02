from turtle import Turtle, Screen

# use https://docs.python.org/3/library/turtle.html

timmy_the_turtle = Turtle()
timmy_the_turtle.shape("turtle")
timmy_the_turtle.color("red")

for _ in range(4):
    timmy_the_turtle.forward(90)
    timmy_the_turtle.right(90)

screen = Screen()
screen.exitonclick()