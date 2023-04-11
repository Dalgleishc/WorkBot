import React from 'react';

const ExerciseCard = ({ exercise }) => {
  return (
    <div className="card">
      <div className="card-body">
        <h5 className="card-title">{exercise.name}</h5>
        <p className="card-text">{exercise.description}</p>
        <p className="card-text"><strong>Duration:</strong> {exercise.duration}</p>
        <p className="card-text"><strong>Difficulty:</strong> {exercise.difficulty}</p>
      </div>
    </div>
  );
}

export default ExerciseCard;
