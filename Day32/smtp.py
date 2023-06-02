import smtplib, random
import datetime as dt

my_email = "eitantravels25@gmail.com"
# you need to go to account security and to app passwords for sockets
# to email sending, eitantravels25@gmail.com -> eitan.brochstein@icloud.com
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

now = dt.datetime.now()
weekday = now.weekday()
if weekday == 0:
    with open("Day32/quotes.txt") as file:
        quote = random.choice(file.read().splitlines())
        sendemail("eitan.brochstein@icloud.com", "Motivational Quote", quote)