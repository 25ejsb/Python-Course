from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self, score):
        super().__init__()
        self.score = score
        self.hideturtle()
        self.speed("fastest")
        self.penup()
        self.goto(-280, 300)
        self.write("Level: " + str(self.score), move=False, align="left", font=("Verdana", 25, "normal"))
    
    def add_level(self):
        self.score += 1
        self.hideturtle()
        self.speed("fastest")
        self.penup()
        self.goto(-280, 300)
        self.write("Level: " + str(self.score), move=False, align="left", font=("Verdana", 25, "normal"))
    
    
    def game_over(self):
        self.penup()
        self.hideturtle()
        self.goto(0, 0)
        self.write("Game Over!", move=False, align="center", font=("Verdana", 25, "normal"))
