import { useEffect, useState } from 'react';
import axios from 'axios';
import { Select } from 'antd';

interface BreedTypeInterface {
  id: number;
  title: string;
}

interface PetSelectProps {
  onChange: (id: number) => void;
  id?: string;
  petType?: number
  value?: number
}

const BreedSelect = (props: PetSelectProps) => {
  const [breedTypes, setBreedTypes] = useState<BreedTypeInterface[]>([]);

  useEffect(() => {
    axios.get('pets/breeds/' + props.petType).then((response) => {
      setBreedTypes(response.data);
    });
  }, [props.petType]);

  return (
    breedTypes && (
      <div className="PetSelect">
        <Select
          size="large"
          id={props.id}
          value={props.value}
          placeholder={"Выберите породу"}
          defaultValue={null}
          onChange={props.onChange}
          options={breedTypes.map((el) => {
            return {
              label: (
                <div>
                  {el.title}
                </div>
              ),
              value: el.id,
            };
          })}
        />
      </div>
    )
  );
};

export default BreedSelect;
