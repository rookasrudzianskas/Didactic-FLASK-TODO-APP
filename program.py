from flask import Flask, render_template


def create_app():
    app = Flask(__name__, static_url_path="", static_folder="css/main.css")

    with app.app_context():
        from mainroutes import routes
        app.register_blueprint(routes)

        return app


