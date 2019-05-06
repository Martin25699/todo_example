from json import JSONEncoder
from todo.model import Todo, Task


class UserJSONEncoder(JSONEncoder):
    def default(self, o):
        if isinstance(o, Todo):
            return {
                "id": o.id,
                "title": o.title,
                "task_list": o.task_list,
            }
        if isinstance(o, Task):
            return {
                "id": o.id,
                "text": o.text,
            }
        return JSONEncoder.default(self, o)
