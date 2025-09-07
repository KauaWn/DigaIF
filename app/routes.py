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


@app.route("/author_single")
def author_single():
    author = {
        "nome": "asdsad",
        "foto": "https://gravatar.com/avatar/27205e5c51cb03f862138b22bcb5dc20f94a342e744ff6df1b8dc8af3c865109"
    }
    return render_template("author_single.html", author_single = author)


@app.route("/author_single2")
def author_single2():
    author = {
        "nome": "afshgadfhfdh",
        "foto": "https://www.gravatar.com/avatar/df5fe0c7d20b494dd2c68e0d8ef9bbf2?s=320&pg&d=identicon"
    }
    return render_template("author_single.html", author_single = author)


@app.route("/contact")
def contact():
    return render_template("contact.html")