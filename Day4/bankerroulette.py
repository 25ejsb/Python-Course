import random
players = input("Players playing the game: ")
split = players.split(", ")

randomPerson = random.randint(0, len(split)-1)
print(f"{split[randomPerson]} is going to buy the meal today!")