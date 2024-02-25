import { useDispatch, useSelector } from 'react-redux';
import { fetchUpdateUser, fetchUser, selectUser } from '../redux/slices/UserSlice';
import { Input } from 'antd';
import { Button } from 'antd';
import React, { Dispatch, SetStateAction, useEffect, useState } from 'react';
import { Link, useNavigate } from 'react-router-dom';
import CitySelect from '../components/global/CitySelect';
import { fetchUpdateSocial } from '../redux/slices/SocialSlice';


const ProfileEdit = () => {
const user = useSelector(selectUser);
  const [username, setUsername] = useState(user.username);
  const [email, setEmail] = useState(user.email);
  const [phone, setPhone] = useState();
  const [password, setPassword] = useState('');
  const [passwordConfirmation, setPasswordConfirmation] = useState('');
  const [name, setName] = useState('');
  const [surname, setSurname] = useState(user.surname);
  const [patronymic, setPatronymic] = useState(user.patronymic);
  const [city_id, setCity] = useState<number>(user.city_id);
  const [telegram, setTelegram] = useState('');
  const [vk, setVk] = useState('');
  const dispatch = useDispatch();
  const navigate = useNavigate();
  const [error, setError] = useState<any>()

useEffect(() => {
    dispatch(fetchUser() as any)
},[dispatch]) 


  const handleSave = () => {

    if (!username) {
      setError("Не указано имя пользователя")
    } else if (!email) {
      setError("Не указан адрес электронной почты")
    } else if (!phone) {
      setError("Не указан адрес электронной почты")
    } else if (!password || !passwordConfirmation) {
      setError("Не указан пароль")
    } else if (password !== passwordConfirmation) {
      setError("Подтверждение пароля не совпадает")
    } else if (!name || !surname || !patronymic) {
      setError("Не указано ФИО")
    } else {
      setError(null)
      dispatch(fetchUpdateUser({ surname, name, patronymic,username, email, city_id}) as any)
      .then(dispatch(fetchUpdateSocial({telegram, vk}) as any))
      .then(
        () => {
          alert("AAAAAAAA")
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
        <h1>Редактировать профиль</h1>

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

        <label htmlFor="telegram">Telegram</label>
        <Input
          size="large"
          id="telegram"
          placeholder={'@telegramTag'}
          value={telegram}
          type="text"
          onChange={(e) => handleChange(e, setTelegram)}
        />

        <label htmlFor="vk">VK</label>
        <Input
          size="large"
          id="vk"
          placeholder={'https://vk.com/yourname'}
          value={vk}
          type="text"
          onChange={(e) => handleChange(e, setVk)}
        />

        <label htmlFor="password-confirm">Подтвердите пароль</label>
        <Input
        size="large"
        id="password-confirm"
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

        <Button type="primary" size="large" onClick={handleSave}>
          Сохранить
        </Button>

        { error && (<div className="Error">{ error }</div>)}

      </div>
    </div>
  );
};

export default ProfileEdit;