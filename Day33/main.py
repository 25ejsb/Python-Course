import requests

# between error code 100, hold on
# between error code 200, Here you go, which is what we got
# between error code 300, access denied, go away
# between error code 400, you screwed up
# between error code 500, computer screwed up

response = requests.get(url="http://api.open-notify.org/iss-now.json")
if response.status_code == 404:
    raise Exception("That resource does not exist")
elif response.status_code == 401:
    raise Exception("You are not authorized to access this data")
response.raise_for_status()

data = response.json()
print(data)
longitude = data["iss_position"]["longitude"]
latitude = data["iss_position"]["latitude"]

iss_position = (longitude, latitude)

print(iss_position)