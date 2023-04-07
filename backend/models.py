from sqlalchemy import Column, Integer, Float, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)
    weight = Column(Float)
    height = Column(Float)
    body_fat_percentage = Column(Float)
    max_bench = Column(Float)
    max_squat = Column(Float)
    max_deadlift = Column(Float)

class MealPlan(Base):
    __tablename__ = 'meal_plans'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer)
    meal = Column(String)
    calories = Column(Integer)

class WorkoutPlan(Base):
    __tablename__ = 'workout_plans'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer)
    workout = Column(String)
    sets = Column(Integer)
    reps = Column(Integer)
    weight = Column(Float)
