from flask import render_template
from app.models import Database
from . import bp


@bp.route("/")
def index():
    db_connection = Database()
    author = db_connection.fetch_all("SELECT * FROM AUTHORS")[0]
    return render_template("index.html", author=author)
