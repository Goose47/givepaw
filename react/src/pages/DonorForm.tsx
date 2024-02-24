import { Dispatch, SetStateAction, useState } from 'react';
import { UploadOutlined } from '@ant-design/icons';
import type { UploadProps } from 'antd';
import { Button, message, Upload } from 'antd';
import { Input } from 'antd';
import { Select, Space } from 'antd';
import type { SelectProps } from 'antd';
import type { RadioChangeEvent } from 'antd';
import { Flex, Radio } from 'antd';
import { Link } from 'react-router-dom';

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

  const handleSelectChange = (value: string[]) => {
    console.log(`selected ${value}`);
  };

  const onChange = (e: RadioChangeEvent) => {
    console.log(`radio checked:${e.target.value}`);
  };

  const props: UploadProps = {
    name: 'file',
    action: 'https://run.mocky.io/v3/435e224c-44fb-4773-9faf-380c5e6a2188',
    headers: {
      authorization: 'authorization-text',
    },
    onChange(info) {
      if (info.file.status !== 'uploading') {
        console.log(info.file, info.fileList);
      }
      if (info.file.status === 'done') {
        message.success(`${info.file.name} file uploaded successfully`);
      } else if (info.file.status === 'error') {
        message.error(`${info.file.name} file upload failed.`);
      }
    },
  };

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
        <Upload {...props}>
          <Button icon={<UploadOutlined />}>Загрузите фото животного</Button>
        </Upload>

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

        <Link to="/profile">
          <Button>Отправить заявку</Button>
        </Link>
      </div>
    </div>
  );
};

export default DonorForm;
