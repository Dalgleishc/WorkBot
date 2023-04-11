import React from 'react';
import PropTypes from 'prop-types';
import { Card, CardHeader, CardBody } from 'reactstrap';

const MealCard = ({ meal }) => {
  const { name, description, imageUrl, calories, carbs, protein, fat } = meal;

  return (
    <Card>
      <CardHeader>
        <h5>{name}</h5>
      </CardHeader>
      <CardBody>
        <img src={imageUrl} alt={name} style={{ maxWidth: '100%', marginBottom: '1rem' }} />
        <p>{description}</p>
        <ul>
          <li>Calories: {calories}</li>
          <li>Carbs: {carbs}g</li>
          <li>Protein: {protein}g</li>
          <li>Fat: {fat}g</li>
        </ul>
      </CardBody>
    </Card>
  );
};

MealCard.propTypes = {
  meal: PropTypes.shape({
    name: PropTypes.string.isRequired,
    description: PropTypes.string.isRequired,
    imageUrl: PropTypes.string.isRequired,
    calories: PropTypes.number.isRequired,
    carbs: PropTypes.number.isRequired,
    protein: PropTypes.number.isRequired,
    fat: PropTypes.number.isRequired,
  }).isRequired,
};

export default MealCard;