from bs4 import BeautifulSoup
import requests, lxml, smtplib

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

URL = "https://www.amazon.com/SkyTech-Chronos-Gaming-Computer-Desktop/dp/B09JBQN8P5/ref=sr_1_4?crid=3NZNUOZEC1Z2R&keywords=gaming%2Bcomputer&qid=1679954988&sprefix=gaming%2Bcomputer%2Caps%2C153&sr=8-4&th=1"

header = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36",
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8"
}
response = requests.get(URL, headers=header)

soup = BeautifulSoup(response.content, "lxml")

output = soup.find(class_="a-offscreen").getText()
outputSplit = int(output.split("$")[1].split(".")[0])
if outputSplit <= 700:
    sendemail("eitantravels25@gmail.com", "This gaming computer is on sale!", f"Buy a new gaming computer for the price of ${outputSplit}. Here is the link: https://www.amazon.com/SkyTech-Chronos-Gaming-Computer-Desktop/dp/B09JBQN8P5/ref=sr_1_4?crid=3NZNUOZEC1Z2R&keywords=gaming%2Bcomputer&qid=1679954988&sprefix=gaming%2Bcomputer%2Caps%2C153&sr=8-4&th=1")