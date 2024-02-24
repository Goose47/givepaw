import { Dispatch, SetStateAction, useState } from 'react';
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

  const handleSelectChange = (value: string[]) => {
    console.log(`selected ${value}`);
  };

  const onChange = (e: RadioChangeEvent) => {
    console.log(`radio checked:${e.target.value}`);
  };

  const handleImageChange = (event: any) => {
    const file = event.target.files[0];
    setImage(file);
  };

  const handleSend = () => {};

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
      <PetSelect />
      <div>
        <div>Тип животного</div>
        <Radio.Group onChange={onChange} defaultValue="a">
          <Radio.Button value="a">кот</Radio.Button>
          <Radio.Button value="b">собака</Radio.Button>
          <Radio.Button value="c">Beijing</Radio.Button>
          <Radio.Button value="d">Chengdu</Radio.Button>
        </Radio.Group>

        <div>Группа крови</div>
        <Radio.Group onChange={onChange} defaultValue="a">
          <Radio.Button value="a">Hangzhou</Radio.Button>
          <Radio.Button value="b">Shanghai</Radio.Button>
          <Radio.Button value="c">Beijing</Radio.Button>
          <Radio.Button value="d">Chengdu</Radio.Button>
        </Radio.Group>

        <div>Компонент крови</div>
        <Radio.Group onChange={onChange} defaultValue="a">
          <Radio.Button value="a">Hangzhou</Radio.Button>
          <Radio.Button value="b">Shanghai</Radio.Button>
          <Radio.Button value="c">Beijing</Radio.Button>
          <Radio.Button value="d">Chengdu</Radio.Button>
        </Radio.Group>

        <Select
          placeholder={'Порода'}
          onChange={(e) => handleChange(e, setBreed)}
          options={[
            { value: 'jack', label: 'Jack' },
            { value: 'lucy', label: 'Lucy' },
            { value: 'Yiminghe', label: 'yiminghe' },
            { value: 'disabled', label: 'Disabled', disabled: true },
          ]}
        />
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
