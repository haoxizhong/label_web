from . import app, login_manager
from application.user import check_user, exist_user, insert_user, User

from flask_login import login_required, login_user, logout_user, current_user
from flask import request, render_template, redirect


@login_manager.user_loader
def load_user(userid):
    if not (exist_user(userid)):
        return None
    else:
        return User(userid)


@app.route("/")
@login_required
def home():
    return render_template("main.html")


@app.route("/logout")
def logout():
    if current_user.is_authenticated:
        logout_user()
    return redirect("/login")


@app.route("/login", methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        return redirect("/")
    if request.method == "GET":
        return render_template("login.html")
    else:
        if not ("username" in request.form) or not ("password" in request.form):
            return render_template("login.html")

        userid = request.form["username"]
        password = request.form["password"]

        if check_user(userid, password):
            login_user(User(userid), True)
            return redirect("/")
        else:
            return render_template("login.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    if current_user.is_authenticated:
        return redirect("/")
    if request.method == "GET":
        return render_template("register.html")
    else:
        if not ("username" in request.form) or not ("password" in request.form):
            return render_template("register.html")

        userid = request.form["username"]
        password = request.form["password"]

        if exist_user(userid):
            UserExistence
        else:
            insert_user(userid, password)
            return redirect("/login")
