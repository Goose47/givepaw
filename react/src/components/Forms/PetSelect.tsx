import { useEffect, useState } from 'react';
import axios from 'axios';
import { Select } from 'antd';

interface PetTypeInterface {
  id: number;
  title: string;
  icon: string;
}

interface PetSelectProps {
  onChange: (id: number) => void;
}

const PetSelect = (props: PetSelectProps) => {
  const [petTypes, setPetTypes] = useState<PetTypeInterface[]>([]);

  useEffect(() => {
    axios.get('pets/pet_types').then((response) => {
      setPetTypes(response.data);
    });
  }, []);

  return (
    petTypes && (
      <div>
        <Select
          onChange={props.onChange}
          options={petTypes.map((el) => {
            return {
              label: (
                <>
                  <img src={el.icon} alt="#" /> {el.title}
                </>
              ),
              value: el.id,
            };
          })}
        />
      </div>
    )
  );
};

export default PetSelect;
