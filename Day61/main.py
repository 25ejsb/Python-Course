from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length
import email_validator

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email("Needs to have a '@' or a '.' in the email")])
    password = PasswordField('Password', validators=[Length(min=8), DataRequired()])
    submit = SubmitField(label="Log In")

def create_app():
    app = Flask(__name__)
    app.secret_key = "fgdjfpkgmkfckdgbn"

    return app

app = create_app()


@app.route("/")
def home():
    return render_template('index.html')

@app.route("/login", methods=["GET", "POST"])
def login():
    login_form = LoginForm()
    if login_form.validate_on_submit():
        if login_form.email.data == "admin@email.com" and login_form.password.data == "12345678":
            return render_template("success.html", form=login_form)
        else:
            return render_template("denied.html", form=login_form)
    return render_template("login.html", form=login_form)

if __name__ == '__main__':
    app.run(debug=True)