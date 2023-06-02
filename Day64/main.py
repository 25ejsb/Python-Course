from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import requests

api_key = "e186220b729c857e1da5bfec3873d268"
api_searchurl = "https://api.themoviedb.org/3/search/movie"
api_url = "https://api.themoviedb.org/3/movie"
details_url = "https://api.themoviedb.org/3/movies/get-movie-details"

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap(app)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///movies-collection.db"
#Optional: But it will silence the deprecation warning in the console.
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    year = db.Column(db.Float, nullable=False)
    description = db.Column(db.String(250), unique=True, nullable=False)
    rating = db.Column(db.Float, nullable=False)
    ranking = db.Column(db.Float, nullable=False)
    review = db.Column(db.String(250), unique=True, nullable=False)
    img_url = db.Column(db.String(1000), unique=True, nullable=False)
    def __init__(self, title, year, description, img_url):
        self.title = title
        self.year = year
        self.description = description
        self.rating = 0
        self.ranking = 0
        self.review = ""
        self.img_url = img_url
    def __repr__(self):
        return f'<Movie {self.title}>'
    
with app.app_context():
    db.create_all()

class RateMovieForm(FlaskForm):
    rating = StringField("Your rating out of 10. e.g 7.5")
    review = StringField("Your review")
    submit = SubmitField("Done")

@app.route("/")
def home():
    all_movies = Movie.query.order_by(Movie.rating).all()
    for i in range(len(all_movies)):
        all_movies[i].ranking = int(len(all_movies) - i)
    db.session.commit()
    return render_template("index.html", movies=all_movies)

@app.route("/edit", methods=["GET", "POST"])
def edit():
    form = RateMovieForm()
    movie_id = request.args.get("id")
    movie = Movie.query.get(movie_id)
    if form.validate_on_submit():
        movie.rating = float(form.rating.data)
        movie.review = form.review.data
        db.session.commit()
        return redirect(url_for('home'))
    return render_template("edit.html", movie=movie, form=form)

@app.route("/delete", methods=["GET", "POST"])
def delete():
    new_id = request.args.get("id")
    movie_to_update = Movie.query.get(new_id)
    db.session.delete(movie_to_update)
    db.session.commit()
    return redirect(url_for('home'))

class SearchMovieForm(FlaskForm):
    title = StringField("Movie Title", validators=[DataRequired()])
    submit = SubmitField("Add Movie")

@app.route("/add", methods=["GET", "POST"])
def add():
    form = SearchMovieForm()
    if form.validate_on_submit():
        movie_title = form.title.data
        response = requests.get(api_searchurl, params={"api_key": api_key, "query": movie_title})
        data = response.json()["results"]
        return render_template("select.html", options=data)
    return render_template("add.html", form=form)

@app.route("/find")
def find():
    movie_id = request.args.get("id")
    if movie_id:
        movie_api_url = f"{api_url}/{movie_id}"
        response = requests.get(movie_api_url, params={"api_key": api_key, "language": "en-US"})
        data = response.json()
        new_title = data["title"]
        if db.session.query(Movie).filter_by(title=new_title).count() < 1:
            new_movie = Movie(
                title=data["title"],
                year=data["release_date"].split("-")[0],
                img_url=f"https://image.tmdb.org/t/p/w500/{data['poster_path']}",
                description=data["overview"],
            )
            db.session.add(new_movie)
            db.session.commit()
    return redirect(url_for('edit', id=new_movie.id))

if __name__ == '__main__':
    app.run(debug=True)
