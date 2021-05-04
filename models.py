from program import db


class TodoList(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False, default="My Todo List")


class TodoItem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
