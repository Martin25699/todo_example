import os
from app import app, db
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

MIGRATION_DIR = os.path.join('migrations')


migrate = Migrate(app, db, directory=MIGRATION_DIR)

manager = Manager(app)
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()
