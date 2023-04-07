from flask import Flask
from flask_cors import CORS

# Import the backend routes and initialize a Flask app
from backend.routes import bp as api

def create_app():
    app = Flask(__name__)
    CORS(app)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///workbot.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.register_blueprint(api)
    return app
