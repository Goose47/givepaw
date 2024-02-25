import { useDispatch, useSelector } from 'react-redux';
import { fetchUpdatePassword, fetchUpdateUser, fetchUser, selectUser } from '../redux/slices/UserSlice';
import { Input } from 'antd';
import { Button } from 'antd';
import React, { Dispatch, SetStateAction, useEffect, useState } from 'react';
import { Link, useNavigate } from 'react-router-dom';
import CitySelect from '../components/global/CitySelect';
import { fetchUpdateSocial } from '../redux/slices/SocialSlice';


const ChangePasswordForm = () => {
const user = useSelector(selectUser);
const [password, setPassword] = useState('');
const [passwordConfirmation, setPasswordConfirmation] = useState('');
  const dispatch = useDispatch();
  const navigate = useNavigate();
  const [error, setError] = useState<any>()

useEffect(() => {
    dispatch(fetchUser() as any)
    console.log(user);

},[dispatch]) 


  const handleSave = () => {

     if (!password || !passwordConfirmation) {
      setError("Не указан пароль")
    } else if (password !== passwordConfirmation) {
      setError("Подтверждение пароля не совпадает")
    } else {
      setError(null)
      dispatch(fetchUpdatePassword({password}) as any)
      .then(
        () => {
          setError(null)
          setTimeout(() => {
            window.location.replace('https://uvuv643.ru/profile');
          }, 300);
        }
      );
  };
};

  const handleChange = (e: React.ChangeEvent<HTMLInputElement>, set: Dispatch<SetStateAction<any>>) => {
    set(e.target.value);
  };

  return (
    <div>
      <div className="Form">
        <h1>Изменить пароль</h1>
        <label htmlFor="password">Новый пароль</label>
        <Input
          size="large"
          id="password"
          placeholder={'Пароль'}
          value={password}
          type="password"
          onChange={(e) => handleChange(e, setPassword)}
        />

        <label htmlFor="password-confirm">Повторите пароль</label>
        <Input
        size="large"
        id="password-confirm"
        placeholder={'Пароль'}
        value={passwordConfirmation}
        type="password"
        onChange={(e) => handleChange(e, setPasswordConfirmation)}
        />
       
        <Button type="primary" size="large" onClick={handleSave}>
          Сохранить
        </Button>

        { error && (<div className="Error">{ error }</div>)}

      </div>
    </div>
  );
};

export default ChangePasswordForm;