from flask import Blueprint, jsonify, request
from flasgger.utils import swag_from
from .model import Todo, Task, db
from def_doc import todo_doc


bp_todo = Blueprint('todo', __name__, url_prefix='/todo')


@bp_todo.route('/list', methods=['GET'])
@swag_from(todo_doc.todo_list)
def todo_list():
    """Возвращает группы задач с их задачами"""
    query = Todo.query

    title_like = request.args.get('title')
    if title_like:
        query = query.filter(Todo.title.like(f"%{title_like}%"))

    per_page = int(request.args.get('per_page'))
    if per_page is not None:
        query = query.limit(per_page)

    page = int(request.args.get('page'))
    if page is not None:
        query = query.offset(page * per_page)

    return jsonify(query.all())


@bp_todo.route('/<int:todo_id>', methods=['GET'])
@swag_from(todo_doc.todo_get)
def todo_get(todo_id):
    """Возвращает группу задач по идентификатору"""
    todo = Todo.query.get(todo_id)
    return jsonify(todo)


@bp_todo.route('/', methods=['POST'])
@swag_from(todo_doc.todo_create)
def todo_create():
    """Создает группу задач с списком задач"""
    todo = Todo(title=request.json.get('title'))
    for task_r in request.json.get('task_list', []):
        task = Task(text=task_r.get('text'), complete=task_r.get('complete', False))
        todo.task_list.append(task)
    db.session.add(todo)
    db.session.commit()
    return jsonify(todo)
