from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("lounge.html")


@app.route("/elixir", methods=["GET"])
def elixir():
    return render_template("elixir.html")


@app.route("/directions", methods=["GET"])
def directions():
    return render_template("directions.html")
