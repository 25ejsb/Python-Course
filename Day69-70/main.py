from flask import Flask, render_template, redirect, url_for, flash, request, abort
from flask_bootstrap import Bootstrap
from flask_ckeditor import CKEditor
from datetime import date
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship
from sqlalchemy import ForeignKey
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user
from forms import CreatePostForm, RegisterForm, LoginForm, CommentForm
from flask_gravatar import Gravatar

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
ckeditor = CKEditor(app)
Bootstrap(app)

from functools import wraps

def admin_only(function):
    @wraps(function)
    def decorated_function(*args, **kwargs):
        if current_user.id != 1:
            return abort(403)
        return function(*args, **kwargs)
    
    return decorated_function

##CONNECT TO DB
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
login_manager = LoginManager(app)

##CONFIGURE TABLES

class User(UserMixin, db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(1000), unique=True)
    password = db.Column(db.String(1000))
    name = db.Column(db.String(1000))
    img = db.Column(db.String(1000))
    posts = relationship("BlogPost", back_populates="author")
    comments = relationship("Comment", back_populates="comment_author")
    def __init__(self, email, password, name, img):
        self.email = email
        self.password = password
        self.name = name
        self.img = img
    def __repr__(self):
        return f"<User {self.email}>"

class BlogPost(db.Model):
    __tablename__ = "blog_posts"
    id = db.Column(db.Integer, primary_key=True)
    author_id = db.Column(db.Integer, ForeignKey("users.id"))
    author = relationship("User", back_populates="posts")
    title = db.Column(db.String(250), unique=True, nullable=False)
    subtitle = db.Column(db.String(250), nullable=False)
    date = db.Column(db.String(250), nullable=False)
    body = db.Column(db.Text, nullable=False)
    img_url = db.Column(db.String(250), nullable=False)
    comments = relationship("Comment", back_populates="parent_post")
    def __init__(self, title, subtitle, body, img_url, author_id, date):
        self.title = title
        self.subtitle = subtitle
        self.body = body
        self.img_url = img_url
        self.author_id = author_id
        self.date = date
    def __repr__(self):
        return f"<BlogPost {self.title}>"
    
class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    post_id = db.Column(db.Integer, ForeignKey("blog_posts.id"))
    author_id = db.Column(db.Integer, ForeignKey("users.id"))
    parent_post = relationship("BlogPost", back_populates="comments")
    comment_author = relationship("User", back_populates="comments")
    text = db.Column(db.Text, nullable=False)
    def __init__(self, text, comment_author, parent_post):
        self.text = text
        self.comment_author = comment_author
        self.parent_post = parent_post
    def __repr__(self):
        return f"<Comment {self.parent_post}>"

with app.app_context():
    db.create_all()

@login_manager.user_loader
def load_user(user_id):
    return db.session.query(User).get(int(user_id))

@app.route('/')
def get_all_posts():
    posts = BlogPost.query.all()
    return render_template("index.html", all_posts=posts, logged_in=current_user.is_authenticated)


@app.route('/register', methods=["GET", "POST"])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        email = str(form.email.data)
        if db.session.query(User).filter_by(email=email).count() < 1:
            new_user = User(
                str(email),
                str(generate_password_hash(form.password.data, method='pbkdf2:sha256', salt_length=8)),
                str(form.name.data),
                str(form.img.data)
            )
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user)
            return redirect(url_for('get_all_posts'))
    return render_template("register.html", form=form)


@app.route('/login', methods=["GET", "POST"])
def login():
    form = LoginForm()
    if request.method == "POST":
        if form.validate_on_submit():
            email = str(form.email.data)
            password = str(form.password.data)
            user = User.query.filter_by(email=email).first()
            if not user:
                flash("This email doesn't exist, Please try again")
            elif not check_password_hash(user.password, password):
                flash("Wrong password, please try again")
                return redirect(url_for('login'))
            else:
                login_user(user)
                return redirect(url_for('get_all_posts'))
    return render_template("login.html", form=form)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('get_all_posts'))


@app.route("/post/<int:post_id>", methods=["GET", "POST"])
def show_post(post_id):
    requested_post = BlogPost.query.get(post_id)
    comment = CommentForm()

    if comment.validate_on_submit():
        if not current_user.is_authenticated:
            flash("You need to login or register to comment")
            return redirect(url_for("login"))
        if str(comment.comment_text.data) != "":
            new_comment = Comment(
                str(comment.comment_text.data),
                current_user,
                requested_post
            )
            if db.session.query(Comment).filter_by(id=new_comment.id).count() < 1:
                db.session.add(new_comment)
                db.session.commit()
    return render_template("post.html", post=requested_post, logged_in=current_user.is_authenticated, comment=comment)


@app.route("/about")
def about():
    return render_template("about.html", logged_in=current_user.is_authenticated)


@app.route("/contact")
def contact():
    return render_template("contact.html", logged_in=current_user.is_authenticated)


@app.route("/new-post", methods=["GET", "POST"])
@admin_only
def add_new_post():
    form = CreatePostForm()
    if form.validate_on_submit():
        new_post = BlogPost(
            str(form.title.data),
            str(form.subtitle.data),
            str(form.body.data),
            str(form.img_url.data),
            str(current_user.id),
            str(date.today().strftime("%B %d, %Y"))
        )
        db.session.add(new_post)
        db.session.commit()
        return redirect(url_for("get_all_posts"))
    return render_template("make-post.html", form=form, logged_in=current_user.is_authenticated)

@app.route("/edit-post/<int:post_id>", methods=["GET", "POST"])
@admin_only
def edit_post(post_id):
    post = BlogPost.query.get(post_id)
    edit_form = CreatePostForm(
        title=str(post.title),
        subtitle=str(post.subtitle),
        img_url=str(post.img_url),
        author=str(post.author.name),
        body=str(post.body)
    )
    if edit_form.validate_on_submit():
        post.title = str(edit_form.title.data)
        post.subtitle = str(edit_form.subtitle.data)
        post.img_url = str(edit_form.img_url.data)
        post.body = str(edit_form.body.data)
        db.session.commit()
        return redirect(url_for("get_all_posts", post_id=post.id))

    return render_template("make-post.html", form=edit_form, logged_in=current_user.is_authenticated)

@app.route("/delete/<int:post_id>")
@admin_only
def delete_post(post_id):
    post_to_delete = BlogPost.query.get(post_id)
    db.session.delete(post_to_delete)
    db.session.commit()
    return redirect(url_for('get_all_posts'))


if __name__ == "__main__":
    app.run(debug=True)
