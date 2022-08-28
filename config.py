from decouple import config
from flask import Flask
from flask_migrate import Migrate
from flask_restful import Api

from db import db
from resources.routs import routes


class ProductionConfig:
    FLASK_ENV = 'prod'
    DEBUG = False
    TESTING = False
    SQLALCHEMY_DATABASE_URI = (
        f'postgresql://{config("DB_USER")}:{config("DB_PASSWORD")}@localhost:{config("DB_PORT")}/{config("DB_NAME")}'
    )


class DevelopmentConfig:
    FLASK_ENV = 'development'
    DEBUG = True
    TESTING = True
    SQLALCHEMY_DATABASE_URI = (
        f'postgresql://{config("DB_USER")}:{config("DB_PASSWORD")}@localhost:{config("DB_PORT")}/{config("DB_NAME")}'
    )


class TestingConfig:
    TESTING = True
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = (
        f'postgresql://{config("TEST_DB_USER")}:{config("TEST_DB_PASSWORD")}'
        f'@localhost:{config("TEST_BD_PORT")}/{config("TEST_DB_NAME")}'
    )


def create_app(conf='config.DevelopmentConfig'):
    app = Flask(__name__)
    db.init_app(app)
    app.config.from_object(conf)
    migrate = Migrate(app, db)

    api = Api(app)
    [api.add_resource(*rout) for rout in routes]
    return app
