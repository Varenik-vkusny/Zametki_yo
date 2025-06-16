import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import CSRFProtect
from flask_migrate import Migrate

db = SQLAlchemy()
csrf = CSRFProtect()
migrate = Migrate()

def create_app():

    app = Flask(__name__, instance_relative_config=True)

    app.config.from_mapping(
        SECRET_KEY = "43ebd1ab942c9baf976fa92eb4750d8d",
        SQLALCHEMY_DATABASE_URI = "sqlite:///data.db"
    )

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    db.init_app(app)
    csrf.init_app(app)
    migrate.init_app(app, db)

    return app