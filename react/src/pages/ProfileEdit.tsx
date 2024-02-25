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
  const [username, setUsername] = useState(user?.username);
  const [email, setEmail] = useState(user?.email);
  const [name, setName] = useState(user?.name);
  const [surname, setSurname] = useState(user?.surname);
  const [patronymic, setPatronymic] = useState(user?.patronymic);
  const [city_id, setCity] = useState<number>(user?.city.id);
  const [telegram, setTelegram] = useState(user?.user_network.telegram);
  const [vk, setVk] = useState(user?.user_network.vk);
  const dispatch = useDispatch();
  const navigate = useNavigate();
  const [error, setError] = useState<any>()

useEffect(() => {
    dispatch(fetchUser() as any)
    console.log(user);

},[dispatch]) 


  const handleSave = () => {

    if (!username) {
      setError("Не указано имя пользователя")
    } else if (!email) {
      setError("Не указан адрес электронной почты")
    } else if (!name || !surname || !patronymic) {
      setError("Не указано ФИО")
    } else {
      setError(null)
      dispatch(fetchUpdateUser({ surname, name, patronymic,username, email, city_id}) as any)
      .then(dispatch(fetchUpdateSocial({telegram, vk}) as any))
      .then(
        (res : any) => {
          if (res.payload) {
            setError(null)
            setTimeout(() => {
              window.location.replace('https://uvuv643.ru/profile');
            }, 300);
          }
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