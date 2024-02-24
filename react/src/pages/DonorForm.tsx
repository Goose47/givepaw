import { Dispatch, SetStateAction, useEffect, useState } from 'react';
import { Button } from 'antd';
import { Input } from 'antd';
import { Select, Space } from 'antd';
import type { SelectProps } from 'antd';
import type { RadioChangeEvent } from 'antd';
import { Flex, Radio } from 'antd';
import { Link, useNavigate } from 'react-router-dom';
import { useDispatch, useSelector } from 'react-redux';
import { selectPets } from '../redux/slices/PetsSlice';
import PetSelect from '../components/Forms/PetSelect';
import MyPetSelect from '../components/Forms/MyPetSelect';
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
  const navigate = useNavigate();

  const [breedOptions, setBreedOptions] = useState<any[]>([]);
  const [animalTypeOptions, setAnimalTypeOptions] = useState<any[]>([]);
  const [bloodComponentOptions, setBloodComponentOptions] = useState<any[]>([]);
  const [bloodGroupOptions, setBloodGroupOptions] = useState<any[]>([]);

  const handleSelectChange = (value: string[]) => {
    console.log(`selected ${value}`);
  };

  const mapBreedOptions = () => {
    let options = breedOptions.map((item) => ({
      value: item.title,
      label: item.title,
    }));
    return options;
  };

  const onChange = (e: RadioChangeEvent) => {
    console.log(`radio checked:${e.target.value}`);
  };

  const onChangeAnimalType = (e: RadioChangeEvent) => {
    setAnimalType(e.target.value);
    setBreedOptions(getBreeds(animalType) as any);
    setBloodGroupOptions(getBloodTypes(animalType) as any);
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

  const handleSend = () => {};

  // useEffect(() => {
  // setAnimalTypeOptions(getAnimalTypes() as any);
  // setBloodComponentOptions(getComponentTypes() as any);
  // setBreedOptions(getBreeds() as any);
  // setBloodGroupOptions(getBloodTypes() as any);
  // },[])

  const options: SelectProps['options'] = [];

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
      <MyPetSelect />
      <div>
        <div>Тип животного</div>
        {animalTypeOptions && (
          <Radio.Group onChange={onChangeAnimalType} defaultValue="a">
            {animalTypeOptions.map((pet) => (
              <div key={pet.id}>
                <Radio.Button value={pet.id}>{pet.title}</Radio.Button>
              </div>
            ))}
          </Radio.Group>
        )}

        <div>Группа крови</div>
        {bloodGroupOptions && (
          <Radio.Group onChange={onChangeBloodGroup} defaultValue="a">
            {bloodGroupOptions.map((group) => (
              <div key={group.id}>
                <Radio.Button value={group.id}>{group.title}</Radio.Button>
              </div>
            ))}
          </Radio.Group>
        )}

        <div>Компонент крови</div>
        {bloodComponentOptions && (
          <Radio.Group onChange={onChangeComponentType} defaultValue="a">
            {bloodComponentOptions.map((component) => (
              <div key={component.id}>
                <Radio.Button value={component.id}>{component.title}</Radio.Button>
              </div>
            ))}
          </Radio.Group>
        )}

        {breedOptions && (
          <Select
            placeholder={'Порода'}
            onChange={(e) => handleChange(e, setBreed)}
            options={(() => mapBreedOptions) as any}
            // options={[
            //   { value: 'jack', label: 'Jack' },
            //   { value: 'lucy', label: 'Lucy' },
            //   { value: 'Yiminghe', label: 'yiminghe' },
            //   { value: 'disabled', label: 'Disabled', disabled: true },
            // ]}
          />
        )}

        <Input placeholder={'Кличка'} value={petName} type="text" onChange={(e) => handleChange(e, setPetName)} />
        <Input placeholder={'Возраст'} value={age} type="text" onChange={(e) => handleChange(e, setAge)} />
        <Input placeholder={'Вес'} value={weight} type="text" onChange={(e) => handleChange(e, setWeight)} />
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
