from . import app

from flask import request, render_template, redirect
import os


@app.route("/", methods=["GET", "POST"])
# @login_required
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
            keyword = "ThisWeekInput" + str(a)
            if keyword in request.form:
                thisWeek.append(request.form[keyword])

            keyword = "NextWeekInput" + str(a)
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
