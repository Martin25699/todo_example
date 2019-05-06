from flask import Flask, jsonify
from flasgger import Swagger
from db import db
import todo
from ext.json_encoder import UserJSONEncoder
from exception import ValidationError

app = Flask(__name__)
app.config.from_pyfile('settings.cfg')
app.config['SWAGGER'] = {
    'title': 'TODO EXAMPLE API',
    'uiversion': 3
}
"""Замена стандартного JSONEncoder
Для прозрачного преобразования моделей БД в JSON"""
app.json_encoder = UserJSONEncoder

"Подключаем приложение Задач к приложению Flask"
todo.init_app(app)

"Подключаем базу данных к приложению Flask"
db.init_app(app)

"Инициируем Swagger для Flask"
swagger = Swagger(app)


@app.errorhandler(ValidationError)
def handle_invalid_usage(error):
    """Обаботчик ошибок, для вывода ошибок валидации"""
    response = jsonify(error.to_dict())
    response.status_code = error.status_code
    return response


if __name__ == '__main__':
    app.run()
