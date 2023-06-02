import random
playerinput = int(input("Enter Rock (0), Paper (1), Scissors (2): "))
computerInput = random.randint(0, 2)

if playerinput == 0 and computerInput == 2:
    print("You chose rock and they chose scissors! You win!")
if playerinput == 0 and computerInput == 1:
    print("You chose rock and they chose paper! You lose!")
if playerinput == 2 and computerInput == 0:
    print("You chose scissors and they chose rock! You lose!")
if playerinput == 1 and computerInput == 0:
    print("You chose paper and they chose rock! You win!")
if playerinput == 2 and computerInput == 1:
    print("You chose scissors and they chose paper! You win!")
if playerinput == 1 and computerInput == 2:
    print("You chose paper and they chose scissors! You lose!")