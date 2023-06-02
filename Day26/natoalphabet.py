import csv
def check_word():
    word = input("Enter a word: ")
    try:
        words = []
        for letter in word:
            words.append(alphabet[letter.upper()])
        print(words)
    except:
        print("Sorry, only letters in the word please")
        check_word()
with open("Day26/nato.csv") as file:
    alphabet = {letter[0]:letter[1] for letter in csv.reader(file)}
    check_word()