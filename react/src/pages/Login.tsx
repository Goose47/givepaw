import React, { Dispatch, SetStateAction, useState } from 'react';
import { Button } from 'antd';
import { Input } from 'antd';
import { Link, useNavigate } from 'react-router-dom';
import { useDispatch } from 'react-redux';
import { fetchLogin } from '../redux/slices/UserSlice';

const Login = () => {
  const [username, setUsername] = useState<string>('');
  const [password, setPassword] = useState<string>('');
  const navigate = useNavigate();
  const dispatch = useDispatch();

  const handleChange = (e: React.ChangeEvent<HTMLInputElement>, set: Dispatch<SetStateAction<any>>) => {
    set(e.target.value);
  };

  const handleLogin = () => {
    dispatch(fetchLogin({ username, password }) as any).then((res : any) => {
      if (res.payload) {
        setTimeout(() => {
          window.location.replace('https://uvuv643.ru/profile');
        }, 300);
      }
    });
  };

  return (
    <>
      <div className="Form">
        <h1>Войти в аккаунт</h1>
        <label htmlFor="username">Имя пользователя</label>
        <Input
          id="username"
          size="large"
          placeholder={'Имя пользователя'}
          value={username}
          type="text"
          onChange={(e) => handleChange(e, setUsername)}
        />
        <label htmlFor="password">Ваш пароль</label>
        <Input
          id="password"
          size="large"
          placeholder={'Пароль'}
          value={password}
          type="password"
          onChange={(e) => handleChange(e, setPassword)}
        />
        <Button size="large" type="primary" onClick={handleLogin}>
          Войти
        </Button>
        <div className="Form__Link">
          <Link to={'/register'}> Нет аккаунта? Зарегистрироваться</Link>
        </div>
      </div>
    </>
  );
};

export default Login;
