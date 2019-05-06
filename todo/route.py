from flask import Blueprint, jsonify, request
from flasgger.utils import swag_from
from .model import Todo, Task, db
from def_doc import todo_doc
from middleware.validator import check_post_with_scheme

bp_todo = Blueprint('todo', __name__, url_prefix='/todo')

TODO_LIST_SCHEME = {
    'title': {'type': 'string', 'required': False},
    'per_page': {'type': 'integer', 'required': False, 'min': 1, 'max': 100, 'coerce': lambda d: int(d)},
    'page': {'type': 'integer', 'required': False, 'min': 0, 'coerce': lambda d: int(d)},
}


@bp_todo.route('/list', methods=['GET'])
@swag_from(todo_doc.todo_list)
@check_post_with_scheme(scheme_query=TODO_LIST_SCHEME)
def todo_list():
    """Возвращает группы задач с их задачами

    :return: результат запроса в виде JSON строки
    :rtype: str
    """
    query = Todo.query

    title_like = request.args.get('title')
    if title_like:
        query = query.filter(Todo.title.like(f"%{title_like}%"))

    per_page = request.args.get('per_page')
    if per_page is not None:
        per_page = int(per_page)
        query = query.limit(per_page)
        page = request.args.get('page')
        if page is not None:
            page = int(page)
            query = query.offset(page * per_page)

    return jsonify(query.all())


@bp_todo.route('/<int:todo_id>', methods=['GET'])
@swag_from(todo_doc.todo_get)
def todo_get(todo_id):
    """Возвращает группу задач по идентификатору

    :param int todo_id: идентификатор группы задач
    :return: результат запроса в виде JSON строки
    :rtype: str
    """
    todo = Todo.query.get(todo_id)
    return jsonify(todo)


TODO_CREATE_SCHEME = {
    'title': {'type': 'string', 'required': True},
    'task_list': {
        'type': 'list',
        'schema': {
            'type': 'dict',
            'schema': {
                'text': {
                    'type': 'string',
                    'required': True,
                },
                'complete': {
                    'type': 'boolean',
                },
            }
        }
    },
}


@bp_todo.route('/', methods=['POST'])
@swag_from(todo_doc.todo_create)
@check_post_with_scheme(schema_json=TODO_CREATE_SCHEME)
def todo_create():
    """Создает группу задач с списком задач
    :return: результат запроса в виде JSON строки
    :rtype: str
    """
    todo = Todo(title=request.json.get('title'))
    for task_r in request.json.get('task_list', []):
        task = Task(text=task_r.get('text'), complete=task_r.get('complete', False))
        todo.task_list.append(task)
    db.session.add(todo)
    db.session.commit()
    return jsonify(todo)
