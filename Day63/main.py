from flask import Flask, render_template, request, redirect, url_for
import sqlite3
from flask_sqlalchemy import SQLAlchemy
db = sqlite3.connect("Day63/new-books-collection.db")
# controls the database
cursor = db.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS books (id INTEGER6 PRIMARY KEY, title varchar(250) NOT NULL UNIQUE, author varchar(250) NOT NULL, rating FLOAT NOT NULL)")
cursor.execute("INSERT OR IGNORE INTO books VALUES(1, 'Harry Potter', 'J.K. Rowling', '9.3')")
db.commit()

app = Flask(__name__)

all_books = []

@app.route('/')
def home():
    return render_template("index.html", books=all_books)


@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "POST":
        new_book = {
            "title": request.form["title"],
            "author": request.form["author"],
            "rating": request.form["rating"],
        }
        all_books.append(new_book)

        return redirect(url_for('home'))
    
    return render_template("add.html")

if __name__ == "__main__":
    app.run(debug=True) 