import React from 'react';

const WorkoutCard = ({ workout }) => {
  return (
    <div className="card">
      <div className="card-header">
        <h3>{workout.name}</h3>
      </div>
      <div className="card-body">
        <div className="workout-card-exercises">
          <h4>Exercises:</h4>
          <ul>
            {workout.exercises.map((exercise) => (
              <li key={exercise.id}>{exercise.name}</li>
            ))}
          </ul>
        </div>
        <div className="workout-card-duration">
          <h4>Duration:</h4>
          <p>{workout.duration} minutes</p>
        </div>
        <div className="workout-card-description">
          <h4>Description:</h4>
          <p>{workout.description}</p>
        </div>
      </div>
    </div>
  );
};

export default WorkoutCard;