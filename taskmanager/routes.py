from flask import render_template
from taskmanager import app, db
from taskmanager.models import Category, Task


@app.route("/")
def Home():
    return render_template("base.html")