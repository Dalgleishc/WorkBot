import React, { useEffect, useState } from 'react';
import { StyleSheet, Text, View, FlatList, SafeAreaView } from 'react-native';
import axios from 'axios';
import MealCard from '../components/MealCard';
import ExerciseCard from '../components/ExerciseCard';
import { globalStyles } from '../styles/GlobalStyles';
import { homeStyles } from '../styles/HomeStyles';

const HomeScreen = () => {
  const [meals, setMeals] = useState([]);
  const [exercises, setExercises] = useState([]);

  useEffect(() => {
    const fetchMeals = async () => {
      const res = await axios.get('http://localhost:5000/api/meals');
      setMeals(res.data);
    };

    const fetchExercises = async () => {
      const res = await axios.get('http://localhost:5000/api/exercises');
      setExercises(res.data);
    };

    fetchMeals();
    fetchExercises();
  }, []);

  return (
    <SafeAreaView style={globalStyles.container}>
      <View style={homeStyles.header}>
        <Text style={homeStyles.title}>WorkBot</Text>
      </View>
      <View style={globalStyles.content}>
        <Text style={globalStyles.subtitle}>Today's Meals</Text>
        <FlatList
          data={meals}
          renderItem={({ item }) => <MealCard meal={item} />}
          keyExtractor={(item) => item.id.toString()}
        />
        <Text style={globalStyles.subtitle}>Today's Exercises</Text>
        <FlatList
          data={exercises}
          renderItem={({ item }) => <ExerciseCard exercise={item} />}
          keyExtractor={(item) => item.id.toString()}
        />
      </View>
    </SafeAreaView>
  );
};

export default HomeScreen;
