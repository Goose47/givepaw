import { Dispatch, SetStateAction, useEffect, useState } from 'react';
import { Button, Input, Radio, Select, Space } from 'antd';

import { useDispatch, useSelector } from 'react-redux';
import { selectPets } from '../redux/slices/PetsSlice';
import type { SelectProps } from 'antd';
import type { RadioChangeEvent } from 'antd';
import { Flex } from 'antd';
import { Link, useNavigate } from 'react-router-dom';
import { getAnimalTypes, getBloodTypes, getBreeds, getComponentTypes } from '../service/data.service';

const DonorForm = () => {
  const [animalType, setAnimalType] = useState('');
  const [breed, setBreed] = useState('');
  const [bloodGroup, setBloodGroup] = useState('');
  const [petName, setPetName] = useState('');
  const [bloodComponent, setBloodComponent] = useState('');
  const [image, setImage] = useState(undefined);
  const [age, setAge] = useState('');
  const [weight, setWeight] = useState('');
  const [vaccinations, setVaccinations] = useState([]);
  const pets = useSelector(selectPets);

  const [breedOptions, setBreedOptions] = useState<any[]>([]);
  const [animalTypeOptions, setAnimalTypeOptions] = useState<any[]>([]);
  const [bloodComponentOptions, setBloodComponentOptions] = useState<any[]>([]);
  const [bloodGroupOptions, setBloodGroupOptions] = useState<any[]>([]);

  const handleSelectChange = (value: string[]) => {
    console.log(`selected ${value}`);
  };

  const onChangeAnimalType = async (e: RadioChangeEvent) => {
    const value = e.target.value;
    setAnimalType(value);

    const breeds = await getBreeds(value);
    setBreedOptions(breeds);

    const bloodTypes = await getBloodTypes(value);
    setBloodGroupOptions(bloodTypes);
  };

  const onChangeBloodGroup = (e: RadioChangeEvent) => {
    setBloodGroup(e.target.value);
  };

  const onChangeComponentType = (e: RadioChangeEvent) => {
    setBloodComponent(e.target.value);
  };

  const handleImageChange = (event: any) => {
    const file = event.target.files[0];
    setImage(file);
  };

  const handleSend = () => {
    // Handle form submission
  };

  useEffect(() => {
    const fetchData = async () => {
      const animalTypes = await getAnimalTypes();
      setAnimalTypeOptions(animalTypes);

      const components = await getComponentTypes();
      setBloodComponentOptions(components);
    };

    fetchData();
  }, []);

  const options = [];

  for (let i = 10; i < 36; i++) {
    options.push({
      label: i.toString(36) + i,
      value: i.toString(36) + i,
    });
  }

  const handleChange = (e: any, set: Dispatch<SetStateAction<any>>) => {
    set(e.target.value);
  };

  return (
    <div>
      <div>Форма донора</div>

      <div>
        {animalTypeOptions && (
          <>
            <div>Тип животного</div>
            <Radio.Group onChange={onChangeAnimalType} defaultValue="a">
              {animalTypeOptions.map((animalType) => (
                <Radio.Button key={animalType.id} value={animalType.id}>{animalType.title}</Radio.Button>
              ))}
            </Radio.Group>
          </>
        )}

        {bloodGroupOptions && (
          <>
            <div>Группа крови</div>
            <Radio.Group onChange={onChangeBloodGroup} defaultValue="a">
              {bloodGroupOptions.map((bloodGroup) => (
                <Radio.Button key={bloodGroup.id} value={bloodGroup.id}>{bloodGroup.title}</Radio.Button>
              ))}
            </Radio.Group>
          </>
        )}

        {bloodComponentOptions && (
          <>
            <div>Компонент крови</div>
            <Radio.Group onChange={onChangeComponentType} defaultValue="a">
              {bloodComponentOptions.map((component) => (
                <Radio.Button key={component.id} value={component.id}>{component.title}</Radio.Button>
              ))}
            </Radio.Group>
          </>
        )}

        {breedOptions && (
          <Select
            placeholder="Порода"
            onChange={(e) => handleChange(e, setBreed)}
            options={breedOptions.map((breed) => ({ value: breed.id, label: breed.title }))}
          />
        )}

        <Input placeholder="Кличка" value={petName} type="text" onChange={(e) => handleChange(e, setPetName)} />
        <Input placeholder="Возраст" value={age} type="text" onChange={(e) => handleChange(e, setAge)} />
        <Input placeholder="Вес" value={weight} type="text" onChange={(e) => handleChange(e, setWeight)} />
        <input type="file" onChange={handleImageChange} />

        <Space style={{ width: '100%' }} direction="vertical">
          <Select
            mode="multiple"
            allowClear
            style={{ width: '100%' }}
            placeholder="Прививки"
            defaultValue={vaccinations}
            onChange={handleSelectChange}
            options={options}
          />
        </Space>
        <Button onClick={handleSend}>Отправить заявку</Button>
      </div>
    </div>
  );
};

export default DonorForm;
