import requests
URL = "https://api.sheety.co/3b701a28dd0c113a99632a3f2190f381/eitansFlightClub/users"
print("Welcome to Eitan's Flight Club\nWe find the best deals and email you.")
data = {
    "user": {
        "firstName": input("Enter your first name: "),
        "lastName": input("Enter your last name: "),
        "email": input("Type your email: ")
    }
}
response = requests.post(URL, json=data)
print(response.text)
print("You're in the club!")