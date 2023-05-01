from flask import Flask, render_template, request
from models import MedievalFactory, FantasyFactory


app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    platoon = []
    if request.method == "POST":
        platoon_type = request.form.get("platoon-type")

        factory = MedievalFactory()

        if platoon_type == "Fantasy":
            factory = FantasyFactory()

        platoon += [
            factory.create_knight(),
            factory.create_archer(),
            factory.create_wizard(),
        ]

    return render_template("index.html", platoon=platoon)
