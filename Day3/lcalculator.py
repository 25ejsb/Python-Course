print("Welcome to the love calculator!")
name1 = input("What is your name? ").lower()
name2 = input("What is their name? ").lower()

names = name1 + name2

countedName1 = names.count("t")
countedName2 = names.count("r")
countedName3 = names.count("u")
countedName4 = names.count("e")
integer1 = countedName1 + countedName2 + countedName3 + countedName4

countedName5 = names.count("l")
countedName6 = names.count("o")
countedName7 = names.count("v")
countedName8 = names.count("e")
integer2 = countedName5 + countedName6 + countedName7 + countedName8

loveScore = str(integer1) + str(integer2)

print(f"Your score is {loveScore}")
if int(loveScore) < 10 or int(loveScore) > 90:
    print("You guys go in like coke and mentos")

if int(loveScore) >= 40 and int(loveScore) <= 50:
    print("You guys are alright together")