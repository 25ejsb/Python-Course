import requests, time, smtplib
from datetime import datetime

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

# paramaters for marblehead, ma
paramaters = {
    "lat": 42.495750,
    "long": -70.863319,
    "formatted": 0
}

response = requests.get(f"https://api.sunrise-sunset.org/json", params=paramaters)
response.raise_for_status()
data = response.json()
sunrise = data["results"]["sunrise"].split("T")[1].split(":")
sunset = data["results"]["sunset"].split("T")[1].split(":")


while True:
    hour = str(datetime.now()).split(" ")[1].split(":")
    if int(hour[0]) == int(sunrise[0]) and int(hour[1]) == int(sunrise[1]):
        sendemail(my_email, "Look Outside!", "The sun is coming up!")
    elif int(hour[0]) == int(sunset[0]) and int(hour[1]) == int(sunset[1]):
        sendemail(my_email, "Look Outside!", "The sun is going down!")
    time.sleep(60)