import React, { useState, useEffect } from 'react';
import { View, Text, StyleSheet, FlatList } from 'react-native';
import ExerciseCard from '../components/ExerciseCard';
import { getExercises } from '../api/exercises';
import { exerciseStyles } from '../styles/ExerciseStyles';

const ExerciseScreen = () => {
  const [exercises, setExercises] = useState([]);

  useEffect(() => {
    fetchExercises();
  }, []);

  const fetchExercises = async () => {
    const exercises = await getExercises();
    setExercises(exercises);
  };

  const renderExercise = ({ item }) => {
    return <ExerciseCard exercise={item} />;
  };

  return (
    <View style={exerciseStyles.container}>
      <Text style={exerciseStyles.title}>Exercises</Text>
      <FlatList
        data={exercises}
        renderItem={renderExercise}
        keyExtractor={(item) => item.id.toString()}
      />
    </View>
  );
};

export default ExerciseScreen;
