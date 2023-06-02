import requests

numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

response = requests.get("https://api.sheety.co/3b701a28dd0c113a99632a3f2190f381/eitan'sBarMitzvahGifts/sheet1")

totalCount = 0
for i in response.json()["sheet1"]:
    split = str(i["gift"])
    if split == "$3k-college fund":
        totalCount += 3000
    else:
        newNum = ""
        for j in split:
            if j in numbers:
                newNum = newNum + j
        if newNum != "":
            totalCount += int(newNum)

print(f"You earned around ${totalCount} from your bar mitzvah including extra gifts")