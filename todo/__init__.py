from .route import bp_todo
from .model import Todo, Task


def init_app(app):
    app.register_blueprint(bp_todo)
