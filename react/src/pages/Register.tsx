import { Input } from 'antd';
import type { UploadProps } from 'antd';
import { UploadOutlined } from '@ant-design/icons';
import { Button, message, Upload } from 'antd';
import React, { Dispatch, SetStateAction, useState } from 'react';
import { Link } from 'react-router-dom';
import CitySelect from '../components/global/CitySelect';
import { useDispatch } from 'react-redux';
import { fetchRegister } from '../redux/slices/UserSlice';

const Register = () => {
  const [username, setUsername] = useState('');
  const [email, setEmail] = useState('');
  const [phone, setPhone] = useState('');
  const [password, setPassword] = useState('');
  const [passwordConfirmation, setPasswordConfirmation] = useState('');
  const [name, setName] = useState('');
  const [surname, setSurname] = useState('');
  const [patronymic, setPatronymic] = useState('');
  const [city, setCity] = useState('');
  const [image, setImage] = useState(undefined);
  const dispatch = useDispatch();

  const handleRegister = () => {
    dispatch(fetchRegister({ username, email, phone, password, name, surname, patronymic, city, image }) as any);
  };

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
      <div className="Form">
        <h1>Зарегистрироваться</h1>

        <label htmlFor="name">Ваше имя</label>
        <Input
          size="large"
          id="name"
          placeholder={'Имя'}
          value={name}
          type="text"
          onChange={(e) => handleChange(e, setName)}
        />

        <label htmlFor="surname">Ваша фамилия</label>
        <Input
          size="large"
          id="surname"
          placeholder={'Фамилия'}
          value={surname}
          type="text"
          onChange={(e) => handleChange(e, setSurname)}
        />

        <label htmlFor="surname">Ваше отчество (необязательно)</label>
        <Input
          size="large"
          id="patronymic"
          placeholder={'Отчество'}
          value={patronymic}
          type="text"
          onChange={(e) => handleChange(e, setPatronymic)}
        />

        <label htmlFor="name">Имя пользователя</label>
        <Input
          size="large"
          id="username"
          placeholder={'Имя пользователя'}
          value={username}
          type="text"
          onChange={(e) => handleChange(e, setUsername)}
        />

        <label htmlFor="surname">Ваш email</label>
        <Input
          size="large"
          id="email"
          placeholder={'Email'}
          value={email}
          type="email"
          onChange={(e) => handleChange(e, setEmail)}
        />

        <label htmlFor="phone">Номер телефона</label>
        <Input
          size="large"
          id="phone"
          placeholder={'Номер телефона'}
          value={phone}
          type="tel"
          onChange={(e) => handleChange(e, setPhone)}
        />

        <label htmlFor="password">Ваш пароль</label>
        <Input
          size="large"
          id="password"
          placeholder={'Пароль'}
          value={password}
          type="text"
          onChange={(e) => handleChange(e, setPassword)}
        />

        <label htmlFor="password-confirm">Подтвердите пароль</label>
        <Input
          size="large"
          id="passowrd-confirm"
          placeholder={'Пароль'}
          value={passwordConfirmation}
          type="text"
          onChange={(e) => handleChange(e, setPasswordConfirmation)}
        />

        <label htmlFor="city_id">Ваш город</label>
        <div className="Form__City">
          <CitySelect size="large" onChange={(e) => handleChange(e, setCity)}>
            <></>
          </CitySelect>
        </div>

        <Upload {...props}>
          <Button size="large" icon={<UploadOutlined />}>
            Загрузите аватарку
          </Button>
        </Upload>

        <Button type="primary" size="large" onClick={handleRegister}>
          Зарегистрироваться
        </Button>

        <div className="Form__Link">
          <Link to={'/login'}>Уже есть аккаунт? Войти</Link>
        </div>
      </div>
    </div>
  );
};

export default Register;
