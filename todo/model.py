from db import db


class Todo(db.Model):
    __tablename__ = 'todo'

    id = db.Column(db.Integer(), primary_key=True)
    title = db.Column(db.String())
    task_list = db.relationship('Task', backref='todo', lazy=True)


class Task(db.Model):
    __tablename__ = 'task'

    id = db.Column(db.Integer(), primary_key=True)
    text = db.Column(db.String())
    todo_id = db.Column(db.Integer(), db.ForeignKey('todo.id'))
    complete = db.Column(db.Boolean(), default=False)
