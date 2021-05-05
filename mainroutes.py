from flask import Flask, Blueprint, app, render_template, redirect, url_for
from models import TodoList, TodoItem
from program import db

routes = Blueprint('routes', __name__)


@routes.route('/lists')
def showLists():
    lists = TodoList.query.all()
    return render_template("showlist.html", todolists=lists)


@routes.route("/addlist")
def addList():
    newList = TodoList()
    newList.name = "New Todo List"
    db.session.add(newList)
    db.session.commit()
    return redirect(url_for('routes.showLists'))


@routes.route('/')
def hello_world():
    items = [
        "Cook dinner",
        "wash Up",
        "Do laundry",
        "Clean Room"
    ]
    return render_template("index.html", todolist=items)
