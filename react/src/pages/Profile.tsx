import { useDispatch, useSelector } from 'react-redux';
import { fetchUser, selectUser } from '../redux/slices/UserSlice';
import React, { useEffect } from 'react';
import { fetchPets, selectPets } from '../redux/slices/PetsSlice';
import PetItem, { Pet } from '../components/global/PetItem';
import { Link, useNavigate } from 'react-router-dom';
import { Button } from 'antd';
import axios from 'axios';
import SocialForm from '../components/global/SocialForm';
import { BiDonateBlood } from "react-icons/bi";
import { MdHealing } from "react-icons/md";

const Profile = () => {
  const dispatch = useDispatch();
  const user = useSelector(selectUser);
  const pets = useSelector(selectPets);

  const navigate = useNavigate();

  useEffect(() => {
    dispatch(fetchUser() as any);
    dispatch(fetchPets() as any);
    console.log(user);
  }, [dispatch]);

  const handleLogout = () => {
    axios.post('auth/logout', {}).then((response) => {
      setTimeout(() => {
        window.location.replace('https://uvuv643.ru/');
      }, 500);
    });
  };

  return (
    user && (
      <div className="Profile">
        <h1>Мой профиль</h1>
        <div className="Profile__Info">
          <div className="Profile__Header">
            <div className="Profile__Header__Avatar">
              <img src="https://http.cat/502" alt="#" />
            </div>
            <div>
              <h2>{user.username}</h2>
              <div>{user.name + ' ' + user.surname + ' ' + user.patronymic}</div>
              <div>{user.email}</div>
              {user.user_network?.telegram && <div>Telegram: {user.user_network.telegram}</div>}
              {user.user_network?.vk && <div>VK: {user.user_network.vk}</div>}
              <div className='Profile__Header__Buttons'>
                <div>
                  <Link to={"/profile-edit"}>
                    <Button type="primary" >
                      Редактировать профиль
                    </Button>
                  </Link>
                </div>
                <div>
                  <Link to={"/password-edit"}>
                    <Button type="primary" >
                      Изменить пароль
                    </Button>
                  </Link>
                </div>
                <div>
                  <Button type="primary" onClick={handleLogout}>
                    Выйти из аккаунта
                  </Button>
                </div>
              </div>
            </div>
          </div>
        </div>
        {pets?.length > 0 ? (
          <div className="Profile__Pets">
            <h3>Мои питомцы:</h3>
            <div className="Profile__Row">
              {pets.map((pet: Pet) => (
                <div className="Profile__Item">
                  <PetItem pet={pet} />
                </div>
              ))}
            </div>

          </div>
        ) : (
          <h4>
            Вы можете <Link to="/donor-form">записать питомца на донорство крови</Link> или{' '}
            <Link to="/recipient-form">оставить заявку, если он нуждается в этом</Link>
          </h4>
        )}

        <div className="HomeHeader__Buttons">
          <Link to={'/donor-form'}>
            <div className="HomeHeader__Button">
              <div>
                <div className="HomeHeader__Button__Icon">
                  <BiDonateBlood />
                </div>
                <div>Стать донором</div>
              </div>
            </div>
          </Link>
          <Link to={'/recipient-form'}>
            <div className="HomeHeader__Button">
              <div>
                <div className="HomeHeader__Button__Icon">
                  <MdHealing />
                </div>
                <div>Нужна кровь</div>
              </div>
            </div>
          </Link>
        </div>
      </div>
    )
  );
};

export default Profile;
