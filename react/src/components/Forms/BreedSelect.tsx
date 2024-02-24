import { useEffect, useState } from 'react';
import axios from 'axios';
import { Select } from 'antd';

interface BreedTypeInterface {
  id: number;
  title: string;
}

interface BreedSelectProps {
  onChange: (id: number) => void;
  petType: number;
}

const BreedSelect = (props: BreedSelectProps) => {
  const [breedTypes, setBreedTypes] = useState<BreedTypeInterface[]>([]);

  useEffect(() => {
    axios.get('/pets/breeds/' + props.petType).then((response) => {
      setBreedTypes(response.data);
    });
  }, []);

  return (
    breedTypes && (
      <div>
        <Select
          onChange={props.onChange}
          options={breedTypes.map((el) => {
            return {
              label: <>{el.title}</>,
              value: el.id,
            };
          })}
        />
      </div>
    )
  );
  return <></>;
};

export default BreedSelect;
