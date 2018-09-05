from . import app, login_manager
from application.user import *

from flask import request, render_template, redirect
from flask_login import login_required, current_user, login_user, logout_user
import os


@app.route("/", methods=["GET", "POST"])
@login_required
def home():
    if request.method == "POST":
        print(request.form)
        if request.form["name"] == "":
            return render_template("main.html", inf="请填写姓名！")

        if not (os.path.exists("log")):
            os.makedirs("log", exist_ok=True)

        path = os.path.join("log", request.form["name"])
        f = open(path, "w")

        thisWeek = []
        nextWeek = []
        for a in range(1, 100):
            keyword = "ThisWeek" + str(a)
            if keyword in request.form:
                thisWeek.append(request.form[keyword])

            keyword = "NextWeek" + str(a)
            if keyword in request.form:
                nextWeek.append(request.form[keyword])

        print("本周工作：", file=f)
        for line in thisWeek:
            print(line, file=f)
        print("下周工作：", file=f)
        for line in thisWeek:
            print(line, file=f)

        f.close()

        return render_template("main.html", inf="提交成功！")

    else:
        return render_template("main.html")


@login_manager.user_loader
def load_user(userid):
    if not (exist_user(userid)):
        return None
    else:
        return User(userid)


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
            return render_template("login.html", inf="请填写用户名和密码！")

        userid = request.form["username"]
        password = request.form["password"]

        if check_user(userid, password):
            login_user(User(userid), True)
            return redirect("/")
        else:
            return render_template("login.html", inf="密码错误！")


@app.route("/register", methods=["GET", "POST"])
def register():
    if current_user.is_authenticated:
        return redirect("/")
    if request.method == "GET":
        return render_template("register.html")
    else:
        if not ("username" in request.form) or not ("password" in request.form):
            return render_template("register.html")
        if request.form["username"] == "" or request.form["password"] == "":
            return render_template("register.html", inf="请输入正确的信息！")

        userid = request.form["username"]
        password = request.form["password"]

        if exist_user(userid):
            return render_template("register.html", inf="用户已存在！")
        else:
            insert_user(userid, password)
            return redirect("/login")
