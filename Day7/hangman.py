import random, wordlist, art, time
word_list = wordlist.word_list
chosenWord = str.lower(word_list[random.randint(0, len(word_list)-1)])
lettersUsed = []
amountDone = 0
lifes = 6

print(art.logo)
print("Welcome to Hangman!")
time.sleep(1)

strlength = len(chosenWord)

for i in range(0, len(chosenWord)):
    if chosenWord[i] == " ":
        strlength -= 1

stages = art.stages

answer = []

for i in range(len(chosenWord)):
    if chosenWord[i] == " ":
        answer.append(" ")
    else:
        answer.append("_")

print(stages[6])

printedAnswer = ""
for i in answer:
    newText = i + " "
    printedAnswer = printedAnswer + newText

print(printedAnswer)

while amountDone < strlength and lifes > 0:
    letter = input("Guess a letter: ").lower()
    letterFalse = False
    letterInWord = False
    letterUsed = ""

    for i in lettersUsed:
        if i == letter:
            letterFalse = True
            letterUsed = i

    for i in range(0, len(chosenWord)):
        if chosenWord[i] == letter:
            letterInWord = True
            break

    if letterInWord == False and letterFalse == False:
        lifes -= 1
        print(stages[6-(6-lifes)])
        print(f"That letter isn't the word, you lost a life! You have {lifes} lives left!")

    if letterFalse == False:
        lettersUsed.append(letter)
        for i in range(len(chosenWord)):
            if chosenWord[i] == letter:
                amountDone += 1
                answer[i] = letter
        
        printedAnswer = ""
        for i in answer:
            newText = i + " "
            printedAnswer = printedAnswer + newText

        print(printedAnswer)
    elif letterFalse == True:
        print("Already guessed that letter!")

if lifes != 0:
    print("You guessed the word, You won!")
else:
    print(f'You ran out of lives, you lost!, The word was "{chosenWord}"')