import { Input } from 'antd';
import type { UploadProps } from 'antd';
import { UploadOutlined } from '@ant-design/icons';
import { Button, message, Upload } from 'antd';
import { Dispatch, SetStateAction, useState } from 'react';
import { Link } from 'react-router-dom';

const Register = () => {
  const [email, setEmail] = useState('');
  const [phone, setPhone] = useState('');
  const [password, setPassword] = useState('');
  const [name, setName] = useState('');
  const [surname, setSurname] = useState('');
  const [patronymic, setPatronymic] = useState('');
  const [city, setCity] = useState('');
  const [image, setImage] = useState(undefined);

  const handleChange = (e: React.ChangeEvent<HTMLInputElement>, set: Dispatch<SetStateAction<any>>) => {
    set(e.target.value);
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

  return (
    <div>
      <div>
        <Input placeholder={'Имя'} value={name} type="text" onChange={(e) => handleChange(e, setName)} />
        <Input placeholder={'Фамилия'} value={surname} type="text" onChange={(e) => handleChange(e, setSurname)} />
        <Input
          placeholder={'Отчество'}
          value={patronymic}
          type="text"
          onChange={(e) => handleChange(e, setPatronymic)}
        />
        <Input placeholder={'Email'} value={email} type="email" onChange={(e) => handleChange(e, setEmail)} />
        <Input placeholder={'Номер телефона'} value={phone} type="tel" onChange={(e) => handleChange(e, setPhone)} />
        <Input placeholder={'Пароль'} value={password} type="text" onChange={(e) => handleChange(e, setPassword)} />
        <Input placeholder={'Город'} value={city} type="text" onChange={(e) => handleChange(e, setCity)} />
        <Upload {...props}>
          <Button icon={<UploadOutlined />}>Загрузите аватарку</Button>
        </Upload>
        <Button>Зарегистрироваться</Button>
        <Link to={'/login'}>Уже есть аккаунт? Войти</Link>
      </div>
    </div>
  );
};

export default Register;
