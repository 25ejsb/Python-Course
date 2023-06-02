players = []
playerNames = []

def enterName(name, bid):
    players.append({name: bid})
    playerNames.append(name)
    question = input("Is there any other players (Y or N)? ")
    if question == "Y":
        enterName(input("What is your name? "), int(input("What is your bid? $")))

enterName(input("What is your name? "), int(input("What is your bid? $")))
biddingRecord = 0
biddingName = ""
for i in range(len(players)):
    if (players[i][playerNames[i]]) > biddingRecord:
        biddingRecord = players[i][playerNames[i]]
        biddingName = playerNames[i]

print(f"The highest bid was {biddingName} with a total of {biddingRecord}.")