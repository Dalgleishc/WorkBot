import axios from 'axios';

const API_BASE_URL = 'http://localhost:5000/api';

export const getMeals = async () => {
  const response = await axios.get(`${API_BASE_URL}/meals`);
  return response.data;
};

export const getExercises = async () => {
  const response = await axios.get(`${API_BASE_URL}/exercises`);
  return response.data;
};

export const createMeal = async (mealData) => {
  const response = await axios.post(`${API_BASE_URL}/meals`, mealData);
  return response.data;
};

export const createExercise = async (exerciseData) => {
  const response = await axios.post(`${API_BASE_URL}/exercises`, exerciseData);
  return response.data;
};

export const deleteMeal = async (mealId) => {
  const response = await axios.delete(`${API_BASE_URL}/meals/${mealId}`);
  return response.data;
};

export const deleteExercise = async (exerciseId) => {
  const response = await axios.delete(`${API_BASE_URL}/exercises/${exerciseId}`);
  return response.data;
};
