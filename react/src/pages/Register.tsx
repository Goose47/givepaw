import { Input } from 'antd';
import { Button } from 'antd';
import React, { Dispatch, SetStateAction, useState } from 'react';
import { Link, useNavigate } from 'react-router-dom';
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
  const [city, setCity] = useState<number>(1);
  const [image, setImage] = useState(undefined);
  const dispatch = useDispatch();
  const navigate = useNavigate();

  const handleRegister = () => {
    
    dispatch(fetchRegister({username, email, phone, password, name, surname, patronymic, city, image }) as any).then(
      () => {
        setTimeout(() => {
          window.location.replace("https://uvuv643.ru/profile");
        }, 300)
      }
    );
  };

  const handleChange = (e: React.ChangeEvent<HTMLInputElement>, set: Dispatch<SetStateAction<any>>) => {
    set(e.target.value);
  };

  const handleImageChange = (event: any) => {
    const file = event.target.files[0];
    setImage(file);
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
          type="password"
          onChange={(e) => handleChange(e, setPassword)}
        />

        <label htmlFor="password-confirm">Подтвердите пароль</label>
        <Input
          size="large"
          id="passowrd-confirm"
          placeholder={'Пароль'}
          value={passwordConfirmation}
          type="password"
          onChange={(e) => handleChange(e, setPasswordConfirmation)}
        />

        <label htmlFor="city_id">Ваш город</label>
        <div className="Form__City">
          <CitySelect size="large" onChange={(value: number) => setCity(value)}>
            <></>
          </CitySelect>
        </div>

        <input type="file" onChange={handleImageChange} />

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
