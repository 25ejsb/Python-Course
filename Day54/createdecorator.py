import time
inputscore = int(input("Score: "))
score = inputscore
adding_score = int(input("Adding Score: "))
def add_score(function):
    def adding_the_score():
        time.sleep(1)
        global adding_score, score
        score += adding_score
        function()
    return adding_the_score

@add_score
def update_score():
    print(f"Your new score is: {score}")

def refresh_score():
    global score
    score = inputscore
    print(f"Refreshed score to: {score}")

update_score()
new_score = add_score(refresh_score)
new_score()