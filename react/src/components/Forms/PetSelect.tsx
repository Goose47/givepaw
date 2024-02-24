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
  id?: string;
}

const PetSelect = (props: PetSelectProps) => {
  const [petTypes, setPetTypes] = useState<PetTypeInterface[]>([]);

  useEffect(() => {
    axios.get('pets/pet_types').then((response) => {
      setPetTypes([{
        id: null, title: "Не выбрано", icon: null,
      }, ...response.data]);
    });
  }, []);

  return (
    petTypes && (
      <div className="PetSelect">
        <Select
          size="large"
          id={props.id}
          placeholder={"Выберите животное"}
          defaultValue={null}
          onChange={props.onChange}
          options={petTypes.map((el) => {
            return {
              label: (
                <div style={{ display: 'flex', alignItems: 'center' }}>
                  { el.icon && <img
                    src={el.icon}
                    alt="#"
                    style={{
                      width: 20,
                      height: 20,
                      marginRight: 15,
                    }}
                  /> }
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

export default PetSelect;
