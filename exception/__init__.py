from http import HTTPStatus


class ValidationError(Exception):
    """Расширение класса исключения для вывода ошибок валидации"""
    status_code = HTTPStatus.BAD_REQUEST

    def __init__(self, errors=None):
        super().__init__(self)
        self.errors = errors

    def to_dict(self):
        return self.errors
