from flask import render_template, request
from app.models import Database
from . import bp


@bp.route("/", methods=["GET", "POST"])
def index():
    database = Database()

    if request.method == "POST":
        book_name = request.form.get("book-name")
        book_description = request.form.get("book-description")
        author_name = request.form.get("author-name")
        author_reference = request.form.get("author-reference")

        author_exists = (
            database.fetch_one(
                f"SELECT COUNT(*) FROM AUTHORS WHERE reference = '{author_reference}'"
            )[0]
            == 1
        )

        if not author_exists:
            database.insert(
                f"INSERT INTO AUTHORS (reference, name) VALUES ('{author_reference}', '{author_name}')"
            )

        database.insert(
            f"INSERT INTO BOOKS (title, description, author_reference) VALUES('{book_name}', '{book_description}', '{author_reference}')"
        )

    catalog = database.fetch_all(
        "SELECT b.title, b.description, a.reference, a.name FROM BOOKS AS b INNER JOIN AUTHORS AS a ON b.author_reference = a.reference"
    )

    print(f"Memory direction for database object: {id(database)}")

    return render_template("index.html", catalog=catalog)
