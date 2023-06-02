from turtle import Screen
from player import Player
from car import Car
from scoreboard import Scoreboard
from time import sleep

screen = Screen()
screen.setup(width=600, height=800)
screen.title("Crossy Road")
screen.tracer(0)

newPlayer = Player(4, 10)
newCar = Car(10)
newScoreboard = Scoreboard(0)
screen.listen()
screen.onkeypress(key="w", fun=newPlayer.movePlayer)

gameIsOn = True
while gameIsOn:
    screen.bgcolor("white")
    screen.update()
    newPlayer.number += 1
    if newPlayer.number == newPlayer.maxNumber:
        newCar.createCar()
        newPlayer.number = 0
    if newPlayer.ycor() >= 380:
        if newPlayer.maxNumber >= 1:
            newPlayer.maxNumber -= 1
            print(newPlayer.maxNumber)
        newCar.speed += 3
        newScoreboard.clear()
        newScoreboard.add_level()
        newPlayer.goto(0, -380)
        for i in newCar.cars:
            i.goto(-10000, i.ycor())
    for i in newCar.cars:
        if i.distance(newPlayer) <= 45:
            gameIsOn = False
            newScoreboard.game_over()
            newPlayer.hideturtle()
        i.goto(i.xcor()-newCar.speed, i.ycor())
    sleep(0.1)

screen.exitonclick()