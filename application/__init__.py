from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_redis import FlaskRedis

from flask_migrate import Migrate

from config import app_config

db = SQLAlchemy()
r = FlaskRedis()
migrate = Migrate(compare_type=True)

def init_app(config):
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object(app_config[config])
    db.init_app(app)
    r.init_app(app)
    migrate.init_app(app, db)

    with app.app_context():

        from .film import film_bp
        app.register_blueprint(film_bp, url_prefix='/film')

        return app
