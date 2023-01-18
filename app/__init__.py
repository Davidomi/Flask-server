from flask import Flask
from flask_mail import Mail
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()
mail = Mail()


def create_app(config_filename='config.Config'):

    app = Flask(__name__)
    app.config.from_object(config_filename)

    db.init_app(app)
    mail.init_app(app)

    with app.app_context():
        db.create_all()
        from app import routes
        app.register_blueprint(routes.bp)

    return app
