from flask import Flask, render_template, request
from datetime import datetime

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():

    age = None

    if request.method == "POST":

        birthdate = request.form["birthdate"]

        birth = datetime.strptime(
            birthdate,
            "%Y-%m-%d"
        )

        today = datetime.today()

        age = today.year - birth.year - (
            (today.month, today.day)
            <
            (birth.month, birth.day)
        )

    return render_template(
        "index.html",
        age=age
    )

if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5000
    )