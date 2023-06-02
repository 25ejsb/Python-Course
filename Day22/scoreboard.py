from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color("white")
        self.speed("fastest")
        self.pensize(10)
        self.goto(0, 300)
        self.right(90)
        self.score1 = 0
        self.score2 = 0
        for i in range(30):
            self.pendown()
            self.forward(10)
            self.penup()
            self.forward(10)
        self.scoreboard = None

    def createScoreboard(self):
        scoreboard = Turtle()
        self.scoreboard = scoreboard
        scoreboard.penup()
        scoreboard.hideturtle()
        scoreboard.speed("fastest")
        scoreboard.color("white")
        scoreboard.goto(0, 250)
        scoreboard.write("0       0", move=False, align="center", font=("Verdana", 25, "normal"))

    def updateScore1(self):
        self.score1 += 1
        self.scoreboard.clear()
        self.scoreboard.write(str(self.score1) + "       " + str(self.score2), move=False, align="center", font=("Verdana", 25, "normal"))

    def updateScore2(self):
        self.score2 += 1
        self.scoreboard.clear()
        self.scoreboard.write(str(self.score1) + "       " + str(self.score2), move=False, align="center", font=("Verdana", 25, "normal"))