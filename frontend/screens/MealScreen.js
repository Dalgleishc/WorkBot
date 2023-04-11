import React, { useState, useEffect } from 'react';
import { StyleSheet, Text, View, FlatList } from 'react-native';
import axios from 'axios';
import MealCard from '../components/MealCard';
import { mealStyles } from '../styles/MealStyles';

const MealScreen = () => {
  const [meals, setMeals] = useState([]);

  useEffect(() => {
    const fetchMeals = async () => {
      const res = await axios.get('http://localhost:5000/api/meals');
      setMeals(res.data);
    };

    fetchMeals();
  }, []);

  return (
    <View style={mealStyles.container}>
      <Text style={mealStyles.title}>Meals</Text>
      <FlatList
        data={meals}
        renderItem={({ item }) => <MealCard meal={item} />}
        keyExtractor={(item) => item.id.toString()}
      />
    </View>
  );
};

export default MealScreen;
