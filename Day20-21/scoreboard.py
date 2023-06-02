from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.score = 0
        self.highscore = 0
        with open("Day20-21/data.txt") as file:
            self.highscore = int(file.read())
        self.goto(0, 250)
        self.updateScoreBoard()

    def updateScoreBoard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.highscore}", move=False, align="center", font=("Verdana", 25, "normal"))

    def resetScore(self):
        if self.score > self.highscore:
            self.highscore = self.score
            with open("Day20-21/data.txt", mode="w") as file:
                file.write(str(self.highscore))
        self.score = 0
        self.updateScoreBoard()

    # def gameOverText(self):
    #     self.goto(0, 0)
    #     self.write("Game Over!", move=False, align="center", font=("Verdana", 25, "normal"))

    def addToScore(self):
        self.score += 1
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.highscore}", move=False, align="center", font=("Verdana", 25, "normal"))