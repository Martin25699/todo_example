from functools import wraps
from flask import request
from cerberus import Validator
from exception import ValidationError


class MyValidator(Validator):
    pass


def _validate(data, scheme):
    """Метод для валидации данных

    :param dict data: словарь данных которые необходимо проверить
    :param scheme: схема проверки словаря данных
    :return: В случае ошибки валидации будет вызывано исключение
    """
    v = MyValidator(scheme)
    if v.validate(data) is False:
        raise ValidationError(v.errors)


def check_post_with_scheme(schema_json=None, schema_path=None, scheme_query=None):
    """Декоратор для валидации входящих данных

    :param dict schema_json: Схема для валидации тела запроса в формате JSON
    :param dict schema_path: Схема для валидации данных в URL строке
    :param dict scheme_query: Схема для валидации данных в параметрах URL строки
    :return:
    """
    def decorator(f):
        @wraps(f)
        def wrapper(*args, **kwargs):
            if schema_json:
                _validate(request.json, schema_json)
            if schema_path:
                _validate(request.view_args, schema_path)
            if scheme_query:
                _validate(dict(request.args), scheme_query)
            return f(*args, **kwargs)

        return wrapper

    return decorator
