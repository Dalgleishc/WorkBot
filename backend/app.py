from flask import Flask, jsonify, request
from flask_jwt_extended import JWTManager, jwt_required, create_access_token, get_jwt_identity

from backend.routes import bp as main_bp
from backend.models import User

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-secret-key-goes-here'
app.config['JWT_SECRET_KEY'] = 'jwt-secret-key-goes-here'

jwt = JWTManager(app)

# Register blueprints for routes
app.register_blueprint(main_bp)

@app.route('/login', methods=['POST'])
def login():
    # Authenticate the user using the provided username and password
    username = request.json.get('username')
    password = request.json.get('password')
    user = User.authenticate(username, password)
    if not user:
        return jsonify({'message': 'Invalid username or password'}), 401
    
    # Generate a JWT token
    access_token = create_access_token(identity=user.id)
    return jsonify({'access_token': access_token}), 200

@app.route('/')
def index():
    return 'Welcome to WorkBot API!'

if __name__ == '__main__':
    app.run()
