#Third party imports

from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

#local imports
from flask_login import LoginManager

from  config import app_config
from flask_bootstrap import Bootstrap

login_manager = LoginManager()

#db variable initialization
db = SQLAlchemy()

def create_app(config_name):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(app_config[config_name])
    app.config.from_pyfile('config.py')
    db.init_app(app)

    # @app.route('/')
    # def hello_world():
    #     return "Hello, World!."

    login_manager.init_app(app)
    login_manager.login_message = "You must be logged in to access this page!."
    login_manager.login_view = "auth.login"

    migrate = Migrate(app, db)
    Bootstrap(app)

    from app import models

    from .admin import admin as admin_blueprint
    app.register_blueprint(admin_blueprint, url_prefix = '/admin')

    from .home import home as home_blueprint
    app.register_blueprint(home_blueprint) #, url_prefix='/home'

    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    return app

