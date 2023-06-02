from flask import Flask, render_template, request
import requests, smtplib

my_email = "eitantravels25@gmail.com"
password = "lkmzeijqholesvam"

app = Flask(__name__)
response = requests.get("https://api.npoint.io/9be5da7060dee44f9046").json()

def sendemail(receiver, subject, message):
    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as connection:
        connection.ehlo()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email, 
            to_addrs=receiver, 
            msg=f"Subject:{subject}\n\n{message}"
        )

@app.route("/")
def home():
    return render_template("index.html", blog=response)

@app.route("/post/<num>")
def get_blog(num):
    return render_template("post.html", blog=response, blognum=int(num)-1, blogimg=response[int(num)-1]["image"])

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route("/form-entry", methods=["POST"])
# Name, Email, Phone, Message
def receive_data():
    name = request.form["name"]
    email = request.form["email"]
    tel = request.form["tel"]
    newmessage = request.form["message"]
    sendemail("eitantravels25@gmail.com", "Contact Information", f"{name},\n{email},\n{tel},\n{newmessage}")
    return render_template("formentry.html")

if __name__ == "__main__":
    app.run(debug=True)