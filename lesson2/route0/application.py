from flask import Flask, render_template, request, session
from flask_session import Session
import sys
import datetime

app = Flask(__name__)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)


# notes = []  # global variable, not a good implementation


@app.route("/")
def index():
    # print(sys.version)
    headline = "Trump is a XXXX."
    return render_template("index.html", headline=headline)
    # return "Hello, world!"


@app.route("/<string:name>")
def hello(name):
    name = name.capitalize()
    return f'<h1>Hello, {name}!!</h1>'


@app.route("/bye")
def bye():
    headline = "Goodbye, Obama."
    return render_template("index.html", headline=headline)


@app.route("/isnewyear")
def isnewyear():
    now = datetime.datetime.now()
    new_year = now.month == 1 and now.date == 1
    new_year = None
    return render_template("index.html", new_year=new_year)


@app.route("/name")
def name():
    names = ["Alice", "Bob", "Casey"]
    return render_template("index.html", names=names)


@app.route("/more1")
def more1():
    return render_template("more1.html")


@app.route("/more2")
def more2():
    return render_template("more2.html")


@app.route("/hello", methods=["GET", "POST"])
def hello_form():
    if request.method == "GET":
        return "Please submit the form instead."
    else:
        name = request.form.get("name")
        return render_template("hello.html", name=name)


@app.route("/note", methods=["GET", "POST"])
def note_func():

    if session.get("notes") is None:
        session["notes"] = []

    if request.method == "GET":
        return render_template("note.html")
    else:
        note = request.form.get("note")
        # notes.append(note)
        # print("note", note)
        session["notes"].append(note)
        return render_template("note.html", notes=session["notes"])
