from flask import Flask

from .config import Config
from .extensions import db, migrate, bcrypt, login_manager

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    db.init_app(app)
    migrate.init_app(app, db)
    bcrypt.init_app(app)
    login_manager.init_app(app)

    login_manager.login_view = 'user.login'
    login_manager.login_message = 'Вы не авторизованы!'

    with app.app_context():
        db.create_all()

    return app
