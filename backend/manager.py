# -*- coding:utf-8 -*-
# Run a test server.
import os
import unittest
import uuid

from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager
from werkzeug.security import generate_password_hash
from werkzeug.serving import run_simple

from app import create_app, db

if os.path.exists('.env'):
    print('Importing environment from .env file')
    for line in open('.env'):
        var = line.strip().split('=')
        if len(var) == 2:
            os.environ[var[0]] = var[1]

app = create_app(os.environ.get("FLATCOKE") or 'development')

manager = Manager(app)
migrate = Migrate(app, db)
manager.add_command('db', MigrateCommand)


@manager.command
def hello():
    """say hello for testing"""
    print('hello')


@manager.command
def recreate_db():
    """
    Recreates a local database. You probably should not use this on
    production.
    """
    db.drop_all()
    db.create_all()
    db.session.commit()


@manager.command
def seed():
    from app.users.models import User, Address
    from faker import Faker
    fake = Faker()
    users = [User(username=fake.user_name(), name=fake.name(),
                  email=fake.email(), password=generate_password_hash("qwer1234", method='sha256'),
                  public_id=str(uuid.uuid4())) for i in range(20)]
    db.session.add_all(users)
    db.session.commit()

    addresses = []
    for user in users:
        address = Address()
        address.user = user
        address.address = fake.address()
        addresses.append(address)
    db.session.add_all(addresses)
    db.session.commit()


@manager.command
def test():
    """Run unit tests."""
    tests = unittest.TestLoader().discover('app.tests', pattern='*.py')
    unittest.TextTestRunner(verbosity=1).run(tests)


@manager.command
def dev():
    # TODO add TestingConfig
    pass


if __name__ == '__main__':
    if os.environ.get('FLATCOKE') == 'production':
        run_simple('0.0.0.0', 5000, app,
                   use_reloader=True, use_debugger=True,
                   )
    manager.run()
