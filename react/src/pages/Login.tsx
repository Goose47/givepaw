import React, { Dispatch, SetStateAction, useState } from 'react';
import { Button } from 'antd';
import { Input } from 'antd';
import { Link } from 'react-router-dom';
import { useDispatch } from 'react-redux';
import { fetchLogin } from '../redux/slices/UserSlice';

const Login = () => {
  const [username, setUsername] = useState<string>('');
  const [password, setPassword] = useState<string>('');
  const dispatch = useDispatch();

  const handleChange = (e: React.ChangeEvent<HTMLInputElement>, set: Dispatch<SetStateAction<any>>) => {
    set(e.target.value);
  };

  const handleLogin = () => {
    dispatch(fetchLogin({ username, password }) as any);
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
          type="text"
          onChange={(e) => handleChange(e, setPassword)}
        />
        <Link to="/profile">
          <Button size="large" type="primary" onClick={handleLogin}>
            Войти
          </Button>
        </Link>
        <div className="Form__Link">
          <Link to={'/register'}> Нет аккаунта? Зарегистрироваться</Link>
        </div>
      </div>
    </>
  );
};

export default Login;
