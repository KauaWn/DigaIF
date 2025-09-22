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
    return render_template("404.html")


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

@app.route("/about-me")
def about_me():
    return render_template("about-me.html")

@app.route("/post-details")
def post_details():
    return render_template("post-details.html")

@app.route("/tags")
def tags():
    return render_template("tags.html")

@app.route("/search-no-results")
def search_no_result():
    return render_template("search-no-result.html")

@app.route("/search-results")
def search_result():
    return render_template("search-result.html")

@app.route("/registro-sucesso")
#O route por ventura não aceita o post por si só, que era o método da tela de login,
#então temos que introduzir na funçao das rotas caso o uso (não foi o caso, mas poderia colocar).
#@app.route("/registro-sucesso", method=['GET','POST']) e fazia um if para colher as informações tipo:
#name = request.form.get('name'), tanto para o nome quanto pra email, senha, etc.
def registrado():
    return render_template("registro-sucesso.html")
#tem que fazer uma condição que se caso já exista tal email, aí não funciona porque já existe uma conta criada, 
#e pra questão de matrícula também (pensar nisso quando for pra usar o mysql)