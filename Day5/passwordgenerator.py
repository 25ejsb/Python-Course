import random

letters = ["a", "b", "c", "d", "e", "f", "g", "h", "l", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
symbols = ["!", "@", "#", "$", "%", "^", "*", "(", ")", "-", "+", "_", "=", ",", "?"]

print("Welcome to the PyPassword Generator")
amountOfLetters = int(input("How long would you like your password: "))
amountOfNumbers = int(input("Enter the amount of numbers you want: "))
amountOfSymbols = int(input("Enter the amount of symbols you want: "))
susPassword = input("Would you like your password to be sus (y or n): ")

listOfCharacters = []
newPassword = ""

amountOfCharacters = amountOfLetters-(amountOfSymbols+amountOfNumbers)

if susPassword == "y":
    letter = "s"
    for i in range(amountOfCharacters):
        newPassword = newPassword + letter
        if letter == "s":
            letter = "u"
        else:
            letter = "s"
else:
    for i in range(amountOfNumbers):
        listOfCharacters.append(str(numbers[random.randint(0, len(numbers)-1)]))

    for i in range(amountOfSymbols):
        listOfCharacters.append(str(symbols[random.randint(0, len(symbols)-1)]))

    for i in range(amountOfCharacters):
        listOfCharacters.append(str(letters[random.randint(0, len(letters)-1)]))

    random.shuffle(listOfCharacters)

    for i in listOfCharacters:
        newPassword = newPassword + i

print(newPassword)