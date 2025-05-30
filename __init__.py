import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_migrate import Migrate

db = SQLAlchemy()
login_manager = LoginManager()
login_manager.login_view = 'auth.login'
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'supersecretkey'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(app.root_path, 'library.db')
    app.config['UPLOAD_FOLDER'] = os.path.join(app.root_path, 'static/uploads')

    db.init_app(app)
    login_manager.init_app(app)
    migrate.init_app(app, db)

    from . import models
    from .models import User

    from .routes import main
    from .auth import auth

    app.register_blueprint(main)
    app.register_blueprint(auth)

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    return app
