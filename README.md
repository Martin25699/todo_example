# todo_example

## Run It
1. Установка зависимостей `pip install -r requirements.txt`
1. Подключение базы данных 
  
    1. Настроить подключение к БД в файле settings.cfg параметр SQLALCHEMY_DATABASE_URI

1. Выполнить обновление БД `python manage.py db upgrade`
1. Запуск приложения в дев режиме `python manage.py`