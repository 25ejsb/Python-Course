from numberguesserart import logo
import random
maxNumber = 100
randomNumber = random.randint(1, maxNumber)

def guessANumber(number):
    if number > randomNumber:
        return "Your guess is too high."
    elif number < randomNumber:
        return "Your guess is too low."
    else:
        return "You guessed the number, You Won!"

def outputNum():
    output = 0
    try:
        output = guessANumber(int(input("Enter a number: ")))
    except:
        print("Bruh, that's not a number")
        outputNum()
    else:
        return output

guesses = 5

def game():
    global guesses
    print(logo)
    print("Welcome to Number Guesser!")
    print(f"Enter a number between 1 and {maxNumber}")
    difficulty = input("Would you like to go on easy mode or hard mode? ")
    if difficulty.lower() == "easy":
        guesses = 10
    print(f"You have {guesses} guesses left.")
    for i in range(guesses):
        output = outputNum()
        print(output)
        guesses -= 1
        if output == "You guessed the number, You Won!":
            return
        print(f"You have {guesses} guesses left.")
    print("You didn't guess the number. You lost!")
    

while True:
    game()
    choice = input("Would you like to play again (y or n)? ")
    if choice == "y":
        randomNumber = random.randint(1, maxNumber)
    else:
        break