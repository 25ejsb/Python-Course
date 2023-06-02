from flask import Flask, render_template
import random, datetime, requests

app = Flask(__name__)

@app.route("/")
def home():
    random_number = random.randint(1, 10)
    return render_template("firstpage.html", num=random_number, year=str(datetime.date.today().year), name="Eitan Brochstein")

@app.route("/guess/<path:name>")
def guess(name):
    gendernew = requests.get(f"https://api.genderize.io/?name={name}").json()["gender"]
    agenew = requests.get(f"https://api.agify.io/?name={name}").json()["age"]
    return render_template("guesser.html", age=agenew, gender=gendernew, name=name)

@app.route("/blog/<num>")
def get_blog(num):
    print(num)
    api_url = "https://api.npoint.io/b9e4ee5e277334a8c04a"
    response = requests.get(api_url)
    all_posts = response.json()
    return render_template("blog.html", posts=all_posts)

if __name__ == "__main__":
    app.run(debug=True)