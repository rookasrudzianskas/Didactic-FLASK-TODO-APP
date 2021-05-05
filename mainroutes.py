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


@routes.route('/list/<listid>')
def viewlist(listid):
    if listid is None:
        return "ERROR"

    list = TodoList.query.filter_by(id=listid).first()
    if list is None:
        return "ERROR"
    return render_template("viewlist.html", todolist=list)
