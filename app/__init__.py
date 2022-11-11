from .routes.auth import auth_bp
from .routes.static import static_bp
from dotenv import load_dotenv
from flask import Flask
from flask_inertia import Inertia
from flask_sqlalchemy import SQLAlchemy
load_dotenv()

app: Flask = Flask(
    __name__,
    template_folder="./templates",
    static_folder="../static/dist"
)

db: SQLAlchemy = SQLAlchemy()
inertia: Inertia = Inertia()

from . import models

def create_app(config) -> Flask:
    app.config.from_object(config)
    inertia.init_app(app)
    app.register_blueprint(auth_bp)
    app.register_blueprint(static_bp)

    with app.app_context():
        db.init_app(app)
        db.create_all()

    return app
