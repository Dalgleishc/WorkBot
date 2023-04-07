from flask import Flask

from .routes import bp as routes_bp
from .chatbot import bp as chatbot_bp


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'mysecretkey'
    app.register_blueprint(routes_bp)
    app.register_blueprint(chatbot_bp)

    return app
