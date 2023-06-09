from flask import Blueprint, jsonify, request
from backend import database as db
from backend.models import User, MealPlan, WorkoutPlan
import nltk
from nltk.chat.util import Chat, reflections

bp = Blueprint('api', __name__, url_prefix='/api')

@bp.route('/workouts', methods=['GET'])
def get_workouts():
    # Query the database to retrieve the user's workout plan based on their input data
    # Return the workout plan as a JSON response
    workouts = Workout.query.all()
    return jsonify([workout.to_dict() for workout in workouts]), 200

@bp.route('/meal-plan', methods=['GET'])
def get_meal_plan():
    # Query the database to retrieve the user's meal plan based on their input data
    # Return the meal plan as a JSON response
    user_id = request.args.get('user_id')  # get user ID from the request parameter
    if user_id:
        user = User.query.get(user_id)
        if not user:
            return jsonify({'error': 'User not found'}), 404
        meal_plans = user.meal_plans.all()  # get all meal plans for the user
    else:
        meal_plans = MealPlan.query.all()  # get all meal plans for all users

    return jsonify([meal_plan.serialize() for meal_plan in meal_plans]), 200

bp = Blueprint('api', __name__, url_prefix='/api')

@bp.route('/chatbot', methods=['POST'])
def chatbot():
    # Get the user's message from the request body
    # Use NLP techniques to analyze the message and provide a response
    # Return the response as a JSON object
    # Get the user's message from the request body
    user_message = request.json['message']

    # Define the pairs and reflections for the chatbot
    pairs = [
        # Greetings
        ["hi|hello|hey", ["Hello!", "Hi there!"]],
        ["what's up|sup|how are you", ["I'm good, thanks for asking!"]],
        ["howdy", ["Howdy partner!"]],
        ["good morning", ["Good morning!"]],
        ["good afternoon", ["Good afternoon!"]],
        ["good evening", ["Good evening!"]],
        
        # Basic questions
        ["who are you", ["I am WorkBot, your personal workout assistant."]],
        ["what can you do", ["I can help you with workout and meal plans. Just ask!"]],
        ["what are some workouts", ["Some workouts include: push-ups, sit-ups, squats, and lunges."]],
        
        # Workout questions
        ["what is a push-up|how to do push-ups", ["Push-ups are an exercise that target your chest, shoulders, and triceps. Here is how to do a proper push-up: ..."]],
        ["what is a sit-up|how to do sit-ups", ["Sit-ups are an exercise that target your abs. Here is how to do a proper sit-up: ..."]],
        ["what is a squat|how to do squats", ["Squats are an exercise that target your legs and glutes. Here is how to do a proper squat: ..."]],
        ["what is a lunge|how to do lunges", ["Lunges are an exercise that target your legs and glutes. Here is how to do a proper lunge: ..."]],
        
        # Meal plan questions
        ["what should I eat for breakfast", ["A healthy breakfast could include eggs, oatmeal, and fruit."]],
        ["what should I eat for lunch", ["A healthy lunch could include a salad with chicken or fish."]],
        ["what should I eat for dinner", ["A healthy dinner could include grilled vegetables and a lean protein like chicken or fish."]],
        
        # Goodbyes
        ["bye|goodbye|see you later|catch you later", ["Goodbye!", "Take care!"]]
    ]

    # Create the chatbot
    chatbot = Chat(pairs, reflections)
    
    # Get the chatbot's response to the user's message
    response = chatbot.respond(user_message)
    
    # Return the response as a JSON object
    return jsonify({"response": response})

@bp.route('/user', methods=['POST'])
def create_user():
    # Create a new user in the database
    # Return the new user's ID as a JSON response
    username = request.json['username']
    email = request.json['email']
    password = request.json['password']
    user = User(username=username, email=email, password=password)
    db.session.add(user)
    db.session.commit()
    return jsonify({'id': user.id}), 201

@bp.route('/user/<int:user_id>', methods=['GET'])
def get_user(user_id):
    # Query the database to retrieve the specified user
    # Return the user's information as a JSON response
    user = User.query.get(user_id)
    if not user:
        return jsonify({'error': 'User not found'}), 404
    return jsonify(user.serialize())

@bp.route('/user/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    # Update the specified user in the database
    # Return the updated user's information as a JSON response
    user = User.query.get(user_id)
    if not user:
        return jsonify({'error': 'User not found'}), 404
    user.username = request.json.get('username', user.username)
    user.email = request.json.get('email', user.email)
    user.password = request.json.get('password', user.password)
    db.session.commit()
    return jsonify(user.serialize())

@bp.route('/user/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    # Delete the specified user from the database
    # Return a success message as a JSON response
    user = User.query.get(user_id)
    if not user:
        return jsonify({'error': 'User not found'}), 404
    db.session.delete(user)
    db.session.commit()
    return jsonify({'message': 'User deleted successfully'}), 200

