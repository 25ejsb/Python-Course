import requests, smtplib, random
URL = "https://api.sheety.co/3b701a28dd0c113a99632a3f2190f381/eitansFlightClub/users"
PLACES = "https://api.sheety.co/3b701a28dd0c113a99632a3f2190f381/eitansFlightClub/places"

my_email = "eitantravels25@gmail.com"
password = "lkmzeijqholesvam"
def sendemail(receiver, subject, message):
    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as connection:
        connection.ehlo()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email, 
            to_addrs=receiver, 
            msg=f"Subject:{subject}\n\n{message}"
        )

response = requests.get(URL)
data = response.json()

response2 = requests.get(PLACES).json()
randomoffer = random.choice(response2['places'])
for i in data["users"]:
    sendemail(i["email"], "New Announcment from Eitan's Flight Club", f"Hello {i['firstName']} {i['lastName']},\n\nWe have a special offer of going to {randomoffer['city']}, and for as low as ${randomoffer['lowestPrice']}\n\nHope you can come!\n\nEitan's Flight Club")