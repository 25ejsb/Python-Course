from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(key="w", fun=snake.w)
screen.onkeypress(key="s", fun=snake.s)
screen.onkeypress(key="a", fun=snake.a)
screen.onkeypress(key="d", fun=snake.d)

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)

    snake.move()

    if snake.head.distance(food) < 15:
        food.refresh()
        scoreboard.addToScore()
        snake.extend()
    
    if snake.head.xcor() > 300 or snake.head.xcor() < -300 or snake.head.ycor() > 300 or snake.head.ycor() < -300:
        scoreboard.resetScore()
        snake.resetSnake()
    
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            scoreboard.resetScore()
            snake.resetSnake()


screen.exitonclick()