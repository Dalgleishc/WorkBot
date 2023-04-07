import datetime


def calculate_bmi(weight, height):
    """
    Calculate BMI given weight (kg) and height (m).
    """
    bmi = weight / (height ** 2)
    return round(bmi, 2)


def calculate_daily_calories(bmi, age, sex, weight, height, activity_level):
    """
    Calculate daily calories needed based on user's BMI, age, sex, weight, height and activity level.
    """
    if sex == 'male':
        bmr = 88.36 + (13.4 * weight) + (4.8 * height * 100) - (5.7 * age)
    else:
        bmr = 447.6 + (9.2 * weight) + (3.1 * height * 100) - (4.3 * age)

    activity_factors = {
        'sedentary': 1.2,
        'lightly_active': 1.375,
        'moderately_active': 1.55,
        'very_active': 1.725,
        'extra_active': 1.9
    }

    daily_calories = bmr * activity_factors[activity_level]

    if bmi < 18.5:
        daily_calories *= 1.2
    elif bmi >= 18.5 and bmi <= 24.9:
        daily_calories *= 1.0
    elif bmi >= 25 and bmi <= 29.9:
        daily_calories *= 0.9
    else:
        daily_calories *= 0.8

    return round(daily_calories, 2)


def generate_workout_plan(user_data):
    """
    Generate a personalized workout plan based on user's input data.
    """
    max_bench = user_data.get('max_bench')
    max_squat = user_data.get('max_squat')
    max_deadlift = user_data.get('max_deadlift')
    body_fat = user_data.get('body_fat')

    # TODO: Implement the algorithm for generating the workout plan based on the user data.

    workout_plan = {
        'day_1': {
            'exercises': [
                {'name': 'Squats', 'sets': 4, 'reps': 8},
                {'name': 'Bench Press', 'sets': 4, 'reps': 8},
                {'name': 'Barbell Rows', 'sets': 4, 'reps': 8},
                {'name': 'Dumbbell Flyes', 'sets': 3, 'reps': 12},
                {'name': 'Plank', 'sets': 3, 'reps': 30}
            ]
        },
        'day_2': {
            'exercises': [
                {'name': 'Deadlifts', 'sets': 4, 'reps': 8},
                {'name': 'Military Press', 'sets': 4, 'reps': 8},
                {'name': 'Pull-Ups', 'sets': 4, 'reps': 8},
                {'name': 'Dumbbell Curls', 'sets': 3, 'reps': 12},
                {'name': 'Crunches', 'sets': 3, 'reps': 30}
            ]
        }
        # TODO: Add more workout plans for other days.
    }

    return workout_plan


def get_current_date():
    """
    Get the current date and time in ISO format.
    """
    return datetime.datetime.now().isoformat()
