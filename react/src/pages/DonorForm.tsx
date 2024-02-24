import React, { Dispatch, SetStateAction, useEffect, useState } from 'react';
import type { RadioChangeEvent } from 'antd';
import { Button, Input, Radio, Select, Space } from 'antd';

import { useSelector } from 'react-redux';
import { selectPets } from '../redux/slices/PetsSlice';
import {
  createPet,
  getAnimalTypes,
  getBloodTypes,
  getBreeds,
  getComponentTypes,
  getVaccines,
} from '../service/data.service';
import { selectUser } from '../redux/slices/UserSlice';

const DonorForm = () => {
  const [animalType, setAnimalType] = useState('');
  const [breed, setBreed] = useState('');
  const [bloodGroup, setBloodGroup] = useState('');
  const [petName, setPetName] = useState('');
  const [bloodComponent, setBloodComponent] = useState('');
  const [image, setImage] = useState('');
  const [age, setAge] = useState('');
  const [weight, setWeight] = useState('');
  const [vaccinations, setVaccinations] = useState<any[]>([]);
  const [vaccinationsOptions, setVaccinationsOptions] = useState([]);
  const pets = useSelector(selectPets);
  const user = useSelector(selectUser);

  const [breedOptions, setBreedOptions] = useState<any[]>([]);
  const [animalTypeOptions, setAnimalTypeOptions] = useState<any[]>([]);
  const [bloodComponentOptions, setBloodComponentOptions] = useState<any[]>([]);
  const [bloodGroupOptions, setBloodGroupOptions] = useState<any[]>([]);

  const handleSelectChange = (value: any) => {
    setBreed(value);
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
    const fetchSend = async () => {
      const pet = await createPet(
        animalType,
        breed,
        bloodGroup,
        petName,
        bloodComponent,
        image,
        age,
        weight,
        vaccinations,
        user
      );
    };
  };

  useEffect(() => {
    const fetchData = async () => {
      const animalTypes = await getAnimalTypes();
      setAnimalTypeOptions(animalTypes);

      const components = await getComponentTypes();
      setBloodComponentOptions(components);

      const vaccinesOptions = await getVaccines();
      setVaccinationsOptions(vaccinationsOptions);
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

  return (
    <div>
      <div className="Form">
        <h1>Форма донора</h1>

        {animalTypeOptions && (
          <>
            <div>Тип животного</div>
            <Radio.Group onChange={onChangeAnimalType} defaultValue="a">
              {animalTypeOptions.map((animalType) => (
                <Radio.Button key={animalType.id} value={animalType.id}>
                  {animalType.title}
                </Radio.Button>
              ))}
            </Radio.Group>
          </>
        )}

        {bloodGroupOptions.length > 1 && (
          <div className="Form__Element">
            <div>Группа крови</div>
            <Radio.Group onChange={onChangeBloodGroup} defaultValue="a">
              {bloodGroupOptions.map((bloodGroup) => (
                <Radio.Button key={bloodGroup.id} value={bloodGroup.id}>
                  {bloodGroup.blood_group.title}, {bloodGroup.rhesus.title}
                </Radio.Button>
              ))}
            </Radio.Group>
          </div>
        )}

        {bloodComponentOptions && (
          <div className="Form__Element">
            <div>Компонент крови</div>
            <Radio.Group onChange={onChangeComponentType} defaultValue="a">
              {bloodComponentOptions.map((component) => (
                <Radio.Button key={component.id} value={component.id}>
                  {component.title}
                </Radio.Button>
              ))}
            </Radio.Group>
          </div>
        )}

        <div className="Form__Element">
          {breedOptions.length > 0 && (
            <Select
              id="breed"
              placeholder="Порода"
              onChange={handleSelectChange}
              options={breedOptions.map((breed) => ({ value: breed.id, label: breed.title }))}
            />
          )}
        </div>

        <label htmlFor="name">Кличка</label>
        <Input
          id="name"
          placeholder="Кличка"
          value={petName}
          type="text"
          onChange={(e) => setPetName(e.target.value)}
        />

        <label htmlFor="age">Возраст</label>
        <Input id="age" placeholder="Возраст" value={age} type="text" onChange={(e) => setAge(e.target.value)} />

        <label htmlFor="weight">Вес</label>
        <Input id="weight" placeholder="Вес" value={weight} type="text" onChange={(e) => setWeight(e.target.value)} />

        <label htmlFor="file">Аватар животного</label>
        <input id="file" type="file" onChange={handleImageChange} />

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

        <Button type="primary" onClick={handleSend}>
          Отправить заявку
        </Button>
      </div>
    </div>
  );
};

export default DonorForm;
