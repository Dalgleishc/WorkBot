import React, { useState, useEffect } from 'react';
import { StyleSheet, View, Text, FlatList, SafeAreaView } from 'react-native';
import axios from 'axios';

import WorkoutCard from '../components/WorkoutCard';
import { globalStyles } from '../styles/GlobalStyles';
import { workoutStyles } from '../styles/WorkoutStyles';

const WorkoutScreen = () => {
  const [workouts, setWorkouts] = useState([]);

  useEffect(() => {
    const fetchWorkouts = async () => {
      const res = await axios.get('http://localhost:5000/api/workouts');
      setWorkouts(res.data);
    };

    fetchWorkouts();
  }, []);

  return (
    <SafeAreaView style={globalStyles.container}>
      <View style={globalStyles.header}>
        <Text style={globalStyles.title}>WorkBot</Text>
      </View>
      <View style={globalStyles.content}>
        <Text style={workoutStyles.subtitle}>Today's Workouts</Text>
        <FlatList
          data={workouts}
          renderItem={({ item }) => <WorkoutCard workout={item} />}
          keyExtractor={(item) => item.id.toString()}
        />
      </View>
    </SafeAreaView>
  );
};

export default WorkoutScreen;
