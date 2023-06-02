from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import inspect
import json

app = Flask(__name__)

##Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

def object_as_dict(obj):
    return {
        c.key: getattr(obj, c.key)
        for c in inspect(obj).mapper.column_attrs
    }

##Cafe TABLE Configuration
class Cafe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=True, nullable=False)
    map_url = db.Column(db.String(500), nullable=False)
    img_url = db.Column(db.String(500), nullable=False)
    location = db.Column(db.String(250), nullable=False)
    seats = db.Column(db.String(250), nullable=False)
    has_toilet = db.Column(db.Boolean, nullable=False)
    has_wifi = db.Column(db.Boolean, nullable=False)
    has_sockets = db.Column(db.Boolean, nullable=False)
    can_take_calls = db.Column(db.Boolean, nullable=False)
    coffee_price = db.Column(db.String(250), nullable=True)
    def __init__(self, name, map_url, img_url, location, seats, has_toilet, has_wifi, has_sockets, can_take_calls, coffee_price):
        self.name = name
        self.map_url = map_url
        self.img_url = img_url
        self.location = location
        self.seats = seats
        self.has_toilet = has_toilet
        self.has_wifi = has_wifi
        self.has_sockets = has_sockets
        self.can_take_calls = can_take_calls
        self.coffee_price = coffee_price
    def __repr__(self):
        return f"<Cafe {self.name}>"


with app.app_context():
    db.create_all()

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/addcafe", methods=["GET", "POST"])
def add_cafe():
    return render_template("add_cafe.html")

## HTTP GET - Read Record

@app.route("/random", methods=["GET"])
def random():
    pass

@app.route("/all")
def all():
    cafes = Cafe.query.all()
    return jsonify(cafes=[object_as_dict(cafe) for cafe in cafes])

@app.route("/update/<int:cafe_id>", methods=["PATCH"])
def update(cafe_id):
    new_price = request.args.get("new_price") # url https://something.com/update?new_price=0
    cafe = db.session.query(Cafe).get(cafe_id)
    if cafe:
        cafe.coffee_price = new_price
        db.session.commit()
        return jsonify(response={"Success": "Successfully uploaded the price."}), 200
    else:
        return jsonify(response={"Not Found": "Sorry, there is no cafe with that id"}), 404

@app.route("/report-closed/<int:cafe_id>", methods=["DELETE"])
def delete_id(cafe_id):
    api_key = request.args.get("api-key")
    if api_key == "TopSecretAPIKey":
        cafe = db.session.query(Cafe).get(cafe_id)
        if cafe:
            db.session.delete(cafe)
            db.session.commit()
            return jsonify(response={"Success": "Deleted Cafe from the database"})
        else:
            return jsonify(response={"Wrong API Key": "Sorry, that's an invalid ID"})
    else:
        return jsonify(response={"Forbidden": "Sorry, that's not the right API Key"})

@app.route("/search")
def search():
    query_location = request.args.get("loc")
    cafe = db.session.query(Cafe).filter_by(location=query_location).first()
    if cafe:
        return jsonify(cafe_is=object_as_dict(cafe))
    else:
        return jsonify(error={"Not Found": "Sorry, we don't have a cafe at that location"})

@app.route("/add", methods=["POST"])
def new_cafe():
    cafe = Cafe(
        str(request.form.get("name")),
        str(request.form.get("map_url")),
        str(request.form.get("img_url")),
        str(request.form.get("loc")),
        str(request.form.get("seats")),
        bool(request.form.get("sockets")),
        bool(request.form.get("toilet")),
        bool(request.form.get("wifi")),
        bool(request.form.get("calls")),
        str(request.form.get("coffee_price"))
    )
    db.session.add(cafe)
    db.session.commit()
    return jsonify(response={"success": "Successfully added the new cafe"})

## HTTP POST - Create Record

## HTTP PUT/PATCH - Update Record

## HTTP DELETE - Delete Record


if __name__ == '__main__':
    app.run(debug=True)