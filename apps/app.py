from flask import Flask


__author__ = ["mmarconm", "Marcelo Marcon"]
__version__ = "1.0.0"

def create_app():

    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object("config.settings")
    app.config.from_pyfile("settings.py", silent=True)


    from apps.views import page
    app.register_blueprint(page, url_prefix="/homepage")


    return app
