from . import app

from flask import request, render_template, redirect


@app.route("/", methods=["GET", "POST"])
# @login_required
def home():
    return render_template("main.html")
