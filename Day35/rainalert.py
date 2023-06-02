# use $env for enviornment variables

OWM_Endpoint = "https://api.openweathermap.org/data/2.5/weather"
api_key = "02d5313f254a2c3a43eb6e398fb5c9a7"
account_sid = "AC867126c1cc6df9793345f8aecccb2852"
auth_token = "059d9391c2eb4f8e313bbaf31d04c26d"

# Use "rgedit" to enable long path support error

import requests
from twilio.rest import Client

weather_params = {
    "lat": 42.495750,
    "lon": -70.863319,
    "appid": api_key,
    "exclude": "current,minutely,daily"
}

response = requests.get(OWM_Endpoint, params=weather_params)
response.raise_for_status()
weather_data = response.json()
weather_slice = weather_data["weather"][0]["id"]
print(weather_slice)
if int(weather_slice) < 750:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body="It's going to rain today! Bring an umbrella!",
        from_='+18884017099',
        to='7812289821'
    )
    print(message.status)