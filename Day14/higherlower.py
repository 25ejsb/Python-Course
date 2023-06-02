from higherlowerart import logo
from higherlowerart import vs
from twitterdict import twitterdict
import random
print(logo)
choice1 = random.choice(twitterdict)
lastPlayer = choice1["Name"]
lastPlayerFollowers = choice1["Followers"]

rightGuesses = 0

def randomdict():
    chosenPlayer = random.choice(twitterdict)
    if chosenPlayer["Name"] == lastPlayer:
        randomdict()
    else:
        return chosenPlayer

def higherlower():
    chosenPlayer = randomdict()
    global lastPlayer, lastPlayerFollowers, rightGuesses
    print(f"{lastPlayer}\n{vs}\n" + chosenPlayer["Name"])
    choice2 = input("Would you like to choose 'A' or 'B'? ")
    if choice2.lower() == "b" and chosenPlayer["Followers"] > lastPlayerFollowers:
        print(f"You guessed correct! " + chosenPlayer["Name"] + f" has more followers than {lastPlayer}")
        lastPlayer = chosenPlayer["Name"]
        lastPlayerFollowers = chosenPlayer["Followers"]
        rightGuesses += 1
        print(f"You guessed {rightGuesses} guesses so far.")
        higherlower()
    elif choice2.lower() == "a" and lastPlayerFollowers > chosenPlayer["Followers"]:
        print(f"You guessed correct! {lastPlayer} has more followers than " + chosenPlayer["Name"])
        lastPlayer = chosenPlayer["Name"]
        lastPlayerFollowers = chosenPlayer["Followers"]
        rightGuesses += 1
        print(f"You guessed {rightGuesses} guesses so far.")
        higherlower()
    else:
        print("Sorry, but you guessed wrong.")
        print(f"You guessed {rightGuesses} guesses correct!")


while True:
    higherlower()
    choice3 = input("Would you like to play again (y or n)? ").lower()
    if choice3 == "y":
        print(logo)
        choice1 = random.choice(twitterdict)
        lastPlayer = choice1["Name"]
        lastPlayerFollowers = choice1["Followers"]
        rightGuesses = 0
    else: break