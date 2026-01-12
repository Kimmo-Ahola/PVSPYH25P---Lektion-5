# Repetition idag
# Bygga en app från grunden?
# Har alla fått igång grundmallen till banken?
# pip install flask
# pip install python-dotenv flask-sqlalchemy flask-migrate pymysql mysql-connector
from flask import Flask, render_template
from flask_migrate import Migrate
from database import db
from dotenv import load_dotenv
import os
import models
from models.book import Book

load_dotenv()

app = Flask(__name__)
# boilerplate = samma sak varje gång
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")
db.init_app(app)
migrate = Migrate(app, db)


@app.route("/book/<int:id>")
def book(id: int):
    book = db.session.query(Book).where(Book.id == id).first()

    return render_template("book.html", book=book)


@app.route("/admin/<id>")
def test(id):
    # get customer by id
    return render_template("admin/index.html")


# Vi ska aldrig skriva domännamnet innan url
# Aldrig skriva: www.minsida.se/ending inuti app.route()
@app.route("/admin")
def home():
    name = "Kimmo"  # name on the right side
    age = 34
    return render_template("admin/index.html", name=name, age=age)


@app.route("/")
def index():
    seeding(db)
    return render_template("index.html")


def seeding(db):
    if db.session.query(Book).first() is None:
        book = Book(title="Title", page_count=5)
        db.session.add(book)
        db.session.commit()


if __name__ == "__main__":
    with app.app_context():
        seeding(db)
    app.run(debug=True)
