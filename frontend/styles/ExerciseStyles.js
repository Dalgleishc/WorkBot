import { StyleSheet } from 'react-native';

const ExerciseStyles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#fff',
    alignItems: 'center',
    justifyContent: 'center',
  },
  title: {
    fontSize: 24,
    fontWeight: 'bold',
    marginBottom: 20,
  },
  exerciseCard: {
    marginBottom: 10,
  },
  addButton: {
    backgroundColor: '#4CAF50',
    borderRadius: 5,
    padding: 10,
    margin: 10,
    alignItems: 'center',
  },
  addButtonText: {
    color: 'white',
    fontWeight: 'bold',
    fontSize: 16,
  },
});

export default ExerciseStyles;
