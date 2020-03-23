
# web_app/routes/book_routes.py

from flask import Blueprint, jsonify, render_template

book_routes = Blueprint("book_routes", __name__)

@book_routes.route("/books.json")
def list_books():
    print("REQUESTED THE BOOKS IN JSON FORMAT")
    books = [
        {"id": 1, "title": "Book 1"},
        {"id": 2, "title": "Book 2"},
        {"id": 3, "title": "Book 3"},
    ] # todo: get from the database
    return jsonify(books)

@book_routes.route("/books")
def books():
    print("VISITED THE BOOKS PAGE")
    books = [
        {"id": 1, "title": "Book 1"},
        {"id": 2, "title": "Book 2"},
        {"id": 3, "title": "Book 3"},
    ] # todo: get from the database
    return render_template("books.html", books=books)
