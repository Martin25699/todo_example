from db import db


class Todo(db.Model):
    """Модель данных для группы задач
    :param int id: идентификатор группы задач
    :param str title: наименование группы задач
    :param list[Task] task_list: список задач в группу задач
    """
    __tablename__ = 'todo'

    id = db.Column(db.Integer(), primary_key=True)
    title = db.Column(db.String())
    task_list = db.relationship('Task', backref='todo', lazy=True)


class Task(db.Model):
    """Модель данных для группы задач
    :param int id: идентификатор задачи
    :param str text: текст задачи
    :param bool complete: флаг завершенности задачи, если завершена то True иначе False
    :param int todo_id: идентификатор группы задач
    """
    __tablename__ = 'task'

    id = db.Column(db.Integer(), primary_key=True)
    text = db.Column(db.String())
    todo_id = db.Column(db.Integer(), db.ForeignKey('todo.id'))
    complete = db.Column(db.Boolean(), default=False)
