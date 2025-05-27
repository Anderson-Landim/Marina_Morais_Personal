from flask import Flask, render_template, url_for
import os

app = Flask(__name__)

@app.route("/")
def home():
    imagens = []
    pasta = os.path.join(app.static_folder, "imagens")
    for nome in os.listdir(pasta):
        if nome.lower().endswith((".jpg", ".jpeg", ".png", ".gif", ".webp")):
            imagens.append(f"imagens/{nome}")
    imagens.sort()  # opcional: organiza por nome
    return render_template("index.html", imagens=imagens)

@app.route("/sobre")
def sobre():
    return render_template("sobre.html")

@app.route("/contato")
def contato():
    return render_template("contato.html")

@app.route("/aulas")
def aulas():
    return render_template("aulas.html")

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
