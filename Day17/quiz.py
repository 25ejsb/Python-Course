gameEnded = False
winner = ""
import random, os, sys

class Player:
    def __init__(self, name):
        self.name = name
        self.correct = 0
        self.incorrect = 0
        self.answers = 0
    
    def incorrectans(self):
        self.incorrect += 1
        self.answers += 1

    def correctans(self):
        global gameEnded, winner
        self.correct += 1
        self.answers += 1
        if self.correct >= 10:
            gameEnded = True
            winner = self.name

class Question:
    def __init__(self, question, answers, correctanswer):
        self.question = question
        self.answers = answers
        self.correctanswer = correctanswer
        self.response = None
        self.correctIndex = None
    
    def askQuestion(self):
        print(self.question)
        for i, answer in enumerate(self.answers):
            print(f"{i+1}. {answer}")
            if answer == self.correctanswer:
                self.correctIndex = i+1
    
    def answerQues(self, res):
        self.response = res
        if res == self.correctanswer or res == str(self.correctIndex):
            return "Correct"
        else:
            return f"Incorrect, the correct answer is {self.correctanswer}"

players = []
def enterPlayer():
    players.append(Player(input("Enter your name. ")))
    choice = input("Are there any other players (y or n)? ")
    if choice.lower() == "y":
        enterPlayer()

enterPlayer()

questions = [
    Question("What is the capital of Germany?", ["Lima", "Berlin", "Amsterdam", "Vienna"], "Berlin"),
    Question("What is the tallest mountain in the world?", ["Mt. Everest", "K2", "Mauna Kea", "Mt. Kilomanjaro"], "Mauna Kea"),
    Question("What is the highest mountain in the world?", ["Mt. Everest", "Cotopaxi", "Chimborazo", "Mt. Kilomanjaro"], "Chimborazo"),
    Question("Who is the best mountaineer in the world? ", ["Nirmal Purja", "Will Gadd", "Colin Haley", "Ed Viesturs"], "Nirmal Purja"),
    Question("When was the end of the war of 1812?", ["1812", "1813", "1814", "1815"], "1814"),
    Question("What is the densest planet in the solar system?", ["Mars", "Earth", "Jupiter", "Uranus"], "Earth"),
    Question("Who is the most followed person on twitter?", ["Elon Musk", "Taylor Swift", "Cristiano Ronaldo", "Barack Obama"], "Barack Obama")
]

index = 0

while not gameEnded:
    player = players[index]
    print(f"{player.name}, your turn.")
    question = random.choice(questions)
    question.askQuestion()
    res = question.answerQues(input("Enter your response. "))
    if res == "Correct":
        player.correctans()
    else:
        player.incorrectans()
    print(res)
    for i in players:
        print(f"{i.name}: {i.correct}")
    index += 1
    if index >= len(players):
        index = 0

print(f"Game Over, {winner} is the winner!")
print("Stats:")
for i in players:
    print(f"{i.name}: {i.correct}/{i.answers} correct.")