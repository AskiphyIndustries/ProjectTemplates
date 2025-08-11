from flask import Flask

from .config import Config
from .extensions import db, migrate, bcrypt, login_manager
from .routes.main import main


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    app.register_blueprint(main)

    db.init_app(app)
    migrate.init_app(app, db)
    bcrypt.init_app(app)

    login_manager.login_view = 'user.login'
    login_manager.login_message = 'Вы не авторизованы!'

    with app.app_context():
        db.create_all()

    return app
