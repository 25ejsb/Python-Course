# sheet link: https://docs.google.com/spreadsheets/d/16aymUHK0DHkNNz0P0CtrMTLvl2OajJP9iSJRCzlTCAg/edit#gid=0

import requests
from datetime import datetime
API_KEY = "1c00f18c89c3bb39245852bba6a5d274"
APP_ID = "8e66c63c"
URL = "https://trackapi.nutritionix.com/v2/natural/exercise"
SHEETY_URL = "https://api.sheety.co/3b701a28dd0c113a99632a3f2190f381/myWorkouts/workouts"

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY
}

json = {
    "query": input("What exersises did you do today? "),
    "gender": "male",
    "weight_kg": 43.0913,
    "height_cm": 164.592,
    "age": 13
}
response = requests.post(URL, json=json, headers=headers)
result = response.json()

now = datetime.now()


json = {
    "workout": {
        "date": now.strftime("%d") + "/" + now.strftime("%m") + "/" + now.strftime("%Y"),
        "time": now.strftime("%I") + ":" + now.strftime("%M") + ":" + now.strftime("%S") + " " + now.strftime("%p"),
        "exercise": result["exercises"][0]["name"].title(),
        "duration": result["exercises"][0]["duration_min"],
        "calories": result["exercises"][0]["nf_calories"],
        "id": result["exercises"][0]["tag_id"]
    }
}

response2 = requests.post(SHEETY_URL, json=json)
print(response2.text)