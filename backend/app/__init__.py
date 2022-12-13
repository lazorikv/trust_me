from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from config import config

from app.s3 import AwsBucketApi

db = SQLAlchemy()
bucket = AwsBucketApi()


def create_app(config_name):
    """For to use dynamic environment"""
    app = Flask(__name__)
    app.config.from_object(config[config_name])

    db.init_app(app)

    # Import a module / component using its blueprint handler variable
    from app.auth.controllers import mod as auth_module
    from app.tenant.controllers import mod as tenant_module
    from app.landlord.controllers import mod as landlord_module
    from app.apartment.controllers import mod as apartment_module
    from app.contract.controllers import mod as contract_module
    from app.address.controllers import mod as address_module
    from app.apartment_photo.controllers import mod as photo_module
    from app.utilitybills.controllers import mod as utilitybills_module

    # Register blueprint(s)
    app.register_blueprint(auth_module)
    app.register_blueprint(tenant_module)
    app.register_blueprint(landlord_module)
    app.register_blueprint(apartment_module)
    app.register_blueprint(contract_module)
    app.register_blueprint(address_module)
    app.register_blueprint(photo_module)
    app.register_blueprint(utilitybills_module)

    return app
