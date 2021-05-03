from flask import Flask, Blueprint, app, render_template

routes = Blueprint('routes', __name__)


@routes.route('/')
def hello_world():
    items = [
        "Cook dinner",
        "wash Up",
        "Do laundry",
        "Clean Room"
    ]
    return render_template("index.html", todolist=items)
