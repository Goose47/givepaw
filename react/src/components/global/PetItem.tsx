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
      <div className="PetItem__Wrapper">
        <div className="PetItem__Avatar">
          <img src="https://http.cat/204" alt={pet.name} />
        </div>
        <div className="PetItem__Data">
          <h3>{pet.name}</h3>
          <div className="Pet__Field">
            <span>Возраст</span>
            <span>{pet.age}</span>
          </div>
          <div className="Pet__Field">
            <span>Вес</span>
            <span>{pet.weight}</span>
          </div>
          <div className="Pet__Field">
            <span>Порода</span>
            <span>{pet.breed}</span>
          </div>
        </div>
      </div>
    </div>
  );
};

export default PetItem;
