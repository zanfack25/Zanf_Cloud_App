from flask import Flask, render_template, request, redirect, url_for, session
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
app.secret_key = "supersecret"  # needed for sessions


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        username = request.form.get("username")
        session["username"] = username
        return redirect(url_for("reaction"))
    return render_template("index.html")


@app.route("/reaction")
def reaction():
    if "username" not in session:
        return redirect(url_for("index"))
    return render_template("reaction.html", username=session["username"])


@app.route("/ball-game")
def ball_game():
    if "username" not in session:
        return redirect(url_for("index"))
    return render_template("ball_game.html", username=session["username"])


@app.route("/health")
def health():
    return "OK", 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
