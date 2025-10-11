from app import app
from flask import render_template, redirect, url_for, request, jsonify
import json
import os
import uuid

postagem = os.path.join(os.path.dirname(__file__), "criar_post.json")

def ler_posts():
    caminho = os.path.join(os.path.dirname(__file__), 'posts.json')
    with open(caminho, 'r', encoding='utf-8') as f:
        return json.load(f)

@app.route('/')
def index():
    posts = ler_posts()  # pega os posts do JSON
    return render_template('index.html', posts=posts)

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
        "nome": "kaua angelo",
        "foto": "https://imgs.search.brave.com/GS83tZwHHu2lC0DP224iGoatEU4ZU5hxltAjnnpw5Ss/rs:fit:500:0:0:0/g:ce/aHR0cHM6Ly91cGxv/YWQud2lraW1lZGlh/Lm9yZy93aWtpcGVk/aWEvY29tbW9ucy90/aHVtYi85Lzk1L1Jh/dWxfU2VpeGFzXyUy/ODE5NzIlMjlfY29s/b3JpemVkLnRpZi9s/b3NzeS1wYWdlMS0y/NTBweC1SYXVsX1Nl/aXhhc18lMjgxOTcy/JTI5X2NvbG9yaXpl/ZC50aWYuanBn"
    }
    return render_template("author_single.html", author_single = author)


@app.route("/author_single2")
def author_single2():
    author = {
        "nome": "alysson daniel",
        "foto": "https://imgs.search.brave.com/CBwHzvh-ox3sw3iK9zdTyCllMyq5xJ8WLSr7a1evqLY/rs:fit:500:0:0:0/g:ce/aHR0cHM6Ly9tLm1l/ZGlhLWFtYXpvbi5j/b20vaW1hZ2VzL00v/TVY1Qk4ySmpZbVl3/T1dVdE9UUTJPUzAw/WTJFMkxXRXdaVFl0/TkRjMVlXRTVOamsy/TldJMFhrRXlYa0Zx/Y0djQC5qcGc"
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

@app.route("/postagem_sucesso", methods=["GET", "POST"])
def postado():
    if request.method == "POST":
        title = request.form.get("title")
        conteudo = request.form.get("conteudo")
        categoria = request.form.get("categoria")

        # transformar em JSON
        dados_json = {
            "id": str(uuid.uuid4()),
            "title": title,
            "conteudo": conteudo,
            "categoria": categoria
        }
        try:
            with open(postagem, "r", encoding="utf-8") as f:
                posts = json.load(f)
        except FileNotFoundError:
            posts = []

        # adiciona a nova postagem
        posts.append(dados_json)

        # salva de volta no arquivo
        with open(postagem, "w", encoding="utf-8") as f:
            json.dump(posts, f, ensure_ascii=False, indent=4)

        return redirect(url_for("criar_post"))  # ou pra onde quiser
    return render_template("criar_post.html")

@app.route("/criar_post")
def criar_post():
    return render_template("criar_post.html")

