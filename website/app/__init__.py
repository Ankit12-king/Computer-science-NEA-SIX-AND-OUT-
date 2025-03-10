from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CSRFProtect

db = SQLAlchemy()
csrf = CSRFProtect()

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')

    db.init_app(app)
    csrf.init_app(app)

    with app.app_context():
        from .routes import main
        app.register_blueprint(main)

        db.create_all()

    return app
