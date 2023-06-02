import turtle, pandas, csv
from turtle import Turtle

screen = turtle.Screen()
screen.bgpic("Day25/states.gif")
screen.title("United States Game")
answers = 0
maxAnswers = 50

class Turtles():
    def game_over(self):
        text = Turtle()
        text.hideturtle()
        text.color("red")
        text.speed("fastest")
        text.goto(0, 0)
        text.write("Game Over!", move=False, align="center", font=("Verdana", 25, "normal"))
        with open("Day25/data.csv", "w") as file:
            writer = csv.writer(file)
            writer.writerow([])
    
    def you_win(self):
        text = Turtle()
        text.hideturtle()
        text.color("green")
        text.speed("fastest")
        text.goto(0, 0)
        text.write("You Win!", move=False, align="center", font=("Verdana", 25, "normal"))
    
    def write_state(self, x, y, state):
        text = Turtle()
        text.hideturtle()
        text.color("black")
        text.speed("fastest")
        text.penup()
        text.goto(x, y)
        text.write(state, move=False, align="center", font=("Verdana", 10, "normal"))

turtles = Turtles()
states = []

with open("Day25/data.csv") as file:
    number = 0
    reader = csv.reader(file)
    for row in reader:
        if row != []:
            number += 1
            states.append(row[0])
            data = pandas.read_csv("Day25/states.csv")
            turtles.write_state(data[data.state == row[0]].x.tolist()[0], data[data.state == row[0]].y.tolist()[0], row[0])
    print(states)
    answers = number
    if states == None:
        states = []

game_is_on = True
while game_is_on:
    answer = "Massachusetts"
    if answers != maxAnswers:
        answer = screen.textinput(title=f"{answers}/{maxAnswers} Correct", prompt="What's a state name, Type 'exit' to save and quit")
    if answer.lower() != None and answer.lower() == "exit":
        game_is_on = False
        screen.bye()
        with open("Day25/data.csv", "w") as file:
            writer = csv.writer(file)
            for i in states:
                writer.writerow([i])
            
    data = pandas.read_csv("Day25/states.csv")
    split = answer.split()
    for i in split:
        i = i.capitalize()
    state = len(data[data["state"] == answer.lower()])
    if state == 0:
        turtles.game_over()
        game_is_on = False
    else:
        if not answer.lower() in states:
            answers += 1
            states.append(answer.lower())
            turtles.write_state(data[data.state == answer.lower()].x.tolist()[0], data[data.state == answer.lower()].y.tolist()[0], answer.lower())
    if answers >= maxAnswers:
        turtles.you_win()
        game_is_on = False

screen.exitonclick()