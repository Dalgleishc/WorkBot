from flask import Flask
from backend.routes import bp as main_bp

app = Flask(__name__)
app.register_blueprint(main_bp, url_prefix='/api')

if __name__ == "__main__":
    app.run(debug=True)
