from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
@app.route("/index")
def home():
    return render_template("/index.html")

@app.route("/quem_somos")
def quem():
    return render_template("/quem_somos.html")

@app.route("/contato")
def cont():
    return render_template("/contato.html")
