from flask import Flask, render_template, request, url_for, redirect, flash, send_from_directory
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user

app = Flask(__name__)

app.config['SECRET_KEY'] = 'any-secret-key-you-choose'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
login_manager = LoginManager(app)

##CREATE TABLE IN DB
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(1000), unique=True)
    password = db.Column(db.String(1000))
    name = db.Column(db.String(1000))
    def __init__(self, email, password, name):
        self.email = email
        self.password = password
        self.name = name
    def __repr__(self):
        return f"<User {self.name}>"
#Line below only required once, when creating DB. 
# db.create_all()

with app.app_context():
    db.create_all()


@app.route('/')
def home():
    return render_template("index.html", logged_in=current_user.is_authenticated)


@app.route('/register', methods=["GET", "POST"])
def register():
    if request.method == "POST":
        new_email = request.form["email"]
        if db.session.query(User).filter_by(email=new_email).count() < 1:
            user = User(
                str(request.form["email"]),
                str(generate_password_hash(request.form["password"], method='pbkdf2:sha256', salt_length=8)),
                str(request.form["name"])
            )
            db.session.add(user)
            db.session.commit()
            login_user(user)
            return redirect(url_for('secrets'))
    return render_template("register.html")

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@app.route('/login', methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]
        user = User.query.filter_by(email=email).first()
        if not user:
            flash("This email doesn't exist, Please try again")
        elif not check_password_hash(user.password, password):
            flash("Password incorrect, Please try again.")
            return redirect(url_for('login'))
        else:
            login_user(user)
            return redirect(url_for('secrets'))
    return render_template("login.html")


@app.route('/secrets', methods=["GET", "POST"])
@login_required
def secrets():
    return render_template("secrets.html", name=current_user.name)


@app.route('/logout')
def logout():
    pass


@app.route('/download', methods=["GET", "POST"])
@login_required
def download():
    return send_from_directory('static', "files/cheat_sheet.pdf")


if __name__ == "__main__":
    app.run(debug=True)
