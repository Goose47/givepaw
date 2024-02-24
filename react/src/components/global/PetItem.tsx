import React from 'react';

export interface Pet {
  "id": 0,
  "blood_group_title": "string",
  "breed_title": "string",
  "pet_type_title": "string",
  "avatar_link": "string",
  "name": "string",
  "age": 0,
  "weight": 0,
  "vaccinations": [
    "string"
  ]
}

interface PetItemProps {
  pet: Pet;
  selectable ?: boolean
}

const PetItem = (props: PetItemProps) => {
  let pet = props.pet;

  return (
    <div className={"PetItem " + (props.selectable ? '_hoverable' : '')}>
      <div className="PetItem__Wrapper">
        <div className="PetItem__Avatar">
          <img src={pet.avatar_link} alt={pet.name} />
        </div>
        <div className="PetItem__Data">
          <h3>{pet.name}</h3>
          <div className="Pet__Field">
            <span>Группа крови</span>
            <span>{pet.blood_group_title}</span>
          </div>
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
            <span>{pet.breed_title}</span>
          </div>
        </div>
      </div>
    </div>
  );
};

export default PetItem;
