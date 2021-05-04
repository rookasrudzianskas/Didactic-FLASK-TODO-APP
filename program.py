from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def create_app():
    app = Flask(__name__, static_url_path="", static_folder="css/main.css")
    app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymsql://rokasusername:admin1234@db4free.net/rokasflaskprojec"
    db.init_app(app)

    with app.app_context():
        from mainroutes import routes
        app.register_blueprint(routes)

        db.create_all()

        return app
