import smtplib, pandas, random
import datetime as dt

# using https://www.pythonanywhere.com to run this every day

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

with open("Day32/birthdays.csv") as file:
    reader = pandas.read_csv(file)
    year = dt.datetime.now().year
    month = dt.datetime.now().month
    newday = dt.datetime.now().day
    for num1, i in enumerate(reader["month"]):
        for num2, j in enumerate(reader["day"]):
            if num1 == num2 and int(i) == month and int(j) == newday:
                with open(f"Day32/letter_templates/letter_{random.randint(1, 3)}.txt") as file2:
                    reader2 = file2.read()
                    msg = reader2.replace("[NAME]", reader["name"][num1])
                    msg = msg.replace("[AGE]", str(int(year)-int(reader["year"][num1])) + "th")
                    sendemail(reader["email"][num1], "Happy Birthday!", msg)