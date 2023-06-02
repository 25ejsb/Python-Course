from flask import Flask, render_template
import requests

app = Flask(__name__)
response = requests.get("https://api.npoint.io/b9e4ee5e277334a8c04a").json()

@app.route('/')
def home():
    return render_template("index.html", blog=response)

@app.route("/post/<num>")
def get_blog(num):
    return render_template("post.html", blog=response, blognum=int(num)-1)

if __name__ == "__main__":
    app.run(debug=True)
