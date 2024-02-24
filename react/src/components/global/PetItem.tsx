import React from 'react';

export interface Pet {
  id: 0;
  blood_group_id: 0;
  breed_id: 0;
  breed: 'string';
  pet_type_id: 0;
  avatar_id: 0;
  name: 'string';
  age: 0;
  weight: 0;
  user_id: 0;
}

interface PetItemProps {
  pet: Pet;
}

const PetItem = (props: PetItemProps) => {
  let pet = props.pet;

  return (
    <div className="PetItem">
      <div className="PetItem__Avatar">
        <img src="https://http.cat/204" alt={pet.name} />
      </div>
      <div className="PetItem__Data">
        <div>{pet.name}</div>
        <div>Возраст: {pet.age}</div>
        <div>Вес: {pet.weight}</div>
        <div>Порода: {pet.breed}</div>
      </div>
    </div>
  );
};

export default PetItem;
