import { useDispatch, useSelector } from 'react-redux';
import { fetchUser, selectUser } from '../redux/slices/UserSlice';
import React, { useEffect } from 'react';
import { fetchPets, selectPets } from '../redux/slices/PetsSlice';
import PetItem, { Pet } from '../components/global/PetItem';
import { Link, useNavigate } from "react-router-dom";
import { Button } from "antd";
import axios from "axios";

const Profile = () => {
  const dispatch = useDispatch();
  const user = useSelector(selectUser);
  const pets = useSelector(selectPets);

  const navigate = useNavigate()

  useEffect(() => {
    dispatch(fetchUser() as any);
    dispatch(fetchPets() as any);
  }, [dispatch]);

  const handleLogout = () => {
    axios.post('auth/logout', {}).then(response => {
      setTimeout(() => {
        window.location.replace("https://uvuv643.ru/");
      }, 500)
    })
  }

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
              <div>{user.name + " " + user.surname + " " + user.patronymic}</div>
              <div>{user.email}</div>
              <div><Button type="link" onClick={handleLogout}>Выйти из аккаунта</Button></div>
            </div>
          </div>
        </div>
        {pets.length > 0 ? (
          <div className="Profile__Pets">
            <h3>Ваши питомцы: </h3>
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
      </div>
    )
  );
};

export default Profile;
