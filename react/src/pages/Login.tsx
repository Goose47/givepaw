import React, { Dispatch, SetStateAction, useState } from 'react';
import { Button } from 'antd';
import { Input } from 'antd';
import { Link } from 'react-router-dom';
import { useDispatch } from 'react-redux';
import { fetchLogin } from '../redux/slices/UserSlice';

const Login = () => {
  const [login, setLogin] = useState<string>('');
  const [password, setPassword] = useState<string>('');
  const dispatch = useDispatch();

  const handleChange = (e: React.ChangeEvent<HTMLInputElement>, set: Dispatch<SetStateAction<any>>) => {
    set(e.target.value);
  };

  const handleLogin = () => {
    dispatch(fetchLogin({ login, password }) as any);
  };

  return (
    <>
      <div className="Form">
        <h1>Войти в аккаунт</h1>
        <label htmlFor="email">Ваш email</label>
        <Input
          id="email"
          size="large"
          placeholder={'Email'}
          value={login}
          type="text"
          onChange={(e) => handleChange(e, setLogin)}
        />
        <label htmlFor="password">Ваш пароль</label>
        <Input
          id="password"
          size="large"
          placeholder={'Пароль'}
          value={password}
          type="text"
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
