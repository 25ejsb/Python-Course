from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
from random import *
import turtle

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
scoreboard = Scoreboard()
scores = scoreboard.createScoreboard()
paddle1 = Paddle("left")
paddle2 = Paddle("right")
ball = Ball("right", "up")

screen.listen()
screen.onkeypress(key="w", fun=paddle1.moveUp)
screen.onkeypress(key="s", fun=paddle1.moveDown)
screen.onkeypress(key="Up", fun=paddle2.moveUp)
screen.onkeypress(key="Down", fun=paddle2.moveDown)
screen.onkeyrelease(key="w", fun=paddle1.stopMoving)
screen.onkeyrelease(key="s", fun=paddle1.stopMoving)
screen.onkeyrelease(key="Up", fun=paddle2.stopMoving)
screen.onkeyrelease(key="Down", fun=paddle2.stopMoving)

game_is_on = True
while game_is_on:
    ball.move()
    if ball.ycor() >= 280:
        ball.verticalang = "down"

    if ball.ycor() <= -280:
        ball.verticalang = "up"
    
    if ball.xcor() >= 400:
        scoreboard.updateScore1()
        ball.goto(0, 0)
        ball.verticalang = "up"
        choices = ["left", "right"]
        ball.direction = choice(choices)

    if ball.xcor() <= -400:
        scoreboard.updateScore2()
        ball.goto(0, 0)
        ball.verticalang = "up"
        choices = ["left", "right"]
        ball.direction = choice(choices)

    if ball.distance(paddle1) <= 70 and ball.xcor() <= -370 or ball.distance(paddle2) <= 70 and ball.xcor() >= 370:
        if ball.direction == "left":
            ball.direction = "right"
        else:
            ball.direction = "left"
        
        if ball.verticalang == "up":
            ball.verticalang = "down"
        else:
            ball.verticalang = "up"

    if paddle1.moving == True:
        if paddle1.movedir == "up":
            if paddle1.ycor() < 250:
                paddle1.goto(paddle1.xcor(), paddle1.ycor()+15)
        if paddle1.movedir == "down":
            if paddle1.ycor() > -250:
                paddle1.goto(paddle1.xcor(), paddle1.ycor()-15)
    
    if paddle2.moving == True:
        if paddle2.movedir == "up":
            if paddle2.ycor() < 250:
                paddle2.goto(paddle2.xcor(), paddle2.ycor()+15)
        if paddle2.movedir == "down":
            if paddle2.ycor() > -250:
                paddle2.goto(paddle2.xcor(), paddle2.ycor()-15)

screen.exitonclick()