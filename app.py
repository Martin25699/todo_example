from flask import Flask
from flasgger import Swagger
from db import db
import todo
from ext.json_encoder import UserJSONEncoder

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://best:best@0.0.0.0:5432/todo_example'
app.config['SWAGGER'] = {
    'title': 'TODO EXAMPLE API',
    'uiversion': 3
}
app.json_encoder = UserJSONEncoder
todo.init_app(app)
db.init_app(app)
swagger = Swagger(app)


if __name__ == '__main__':
    app.run()
