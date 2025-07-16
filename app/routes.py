from app import app
from flask import render_template


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/terms")
def terms():
    return render_template("terms_conditions.html")


@app.route("/error404")
def error404():
    return render_template("index.html")