from blackjackart import logo
import random
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
playerCards, computerCards = [], []
def drawCard(): 
    return random.choice(cards)
print(logo)
computerCards.append(drawCard())
computerCards.append(drawCard())
playerCards.append(drawCard())
playerCards.append(drawCard())
def blackjack():
    print(f"You cards: {playerCards}")
    print(f"Computers first number: {computerCards[0]}")
    userChoice = input("Would you like to pick up another card (y or n)? ")
    if userChoice.lower() == "y":
        computerNewCard = drawCard()
        addUp = 0
        for i in computerCards:
            addUp += i
        addUp += computerNewCard
        if addUp <= 21:
            computerCards.append(computerNewCard)
        playerCards.append(drawCard())
        addedUp = 0
        for i in playerCards:
            addedUp += i
        if addedUp > 21:
            print(f"You cards: {playerCards}")
            print(f"Computers cards: {computerCards}")
            print("You went over. You Lose")
            return
        else:
            blackjack()
    if userChoice.lower() == "n":
        playerAddedUp = 0
        for i in playerCards:
            playerAddedUp += i
        computerAddedUp = 0
        for i in computerCards:
            computerAddedUp += i
        if playerAddedUp > computerAddedUp:
            print(f"You cards: {playerCards}")
            print(f"Computers cards: {computerCards}")
            print("You win!")
        elif playerAddedUp == computerAddedUp:
            print(f"You cards: {playerCards}")
            print(f"Computers cards: {computerCards}")
            print("You drawed")
        else:
            print(f"You cards: {playerCards}")
            print(f"Computers cards: {computerCards}")
            print("You Lose")

while True:
    blackjack()
    choice = input("Would you like to play again (y or n)? ")
    if choice.lower() == "y":
        computerCards = []
        playerCards = []
        print(logo)
        computerCards.append(drawCard())
        computerCards.append(drawCard())
        playerCards.append(drawCard())
        playerCards.append(drawCard())
    if choice.lower() == "n": break