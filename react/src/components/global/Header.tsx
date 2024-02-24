import React, { useEffect } from 'react';
import { Link } from 'react-router-dom';
import { Button } from 'antd';
import { BsGeoAltFill } from 'react-icons/bs';
import CitySelect from './CitySelect';
import { useDispatch, useSelector } from 'react-redux';
import { fetchUser, selectUser } from '../../redux/slices/UserSlice';

const Header = () => {
  const user = useSelector(selectUser);
  const dispatch = useDispatch();

  useEffect(() => {
    dispatch(fetchUser() as any);
  }, [dispatch]);

  return (
    <header className="Header">
      <div className="container">
        <div className="Header__Wrapper">
          <div className="Header__Left">
            <Link to={'/'}>
              <div className="Header__Logo">
                <img src="images/logo.svg" alt="Donor Search" />
              </div>
            </Link>
            <Link to="/haha">Как стать донором?</Link>
            <Link to="/haha">Как сдать кровь?</Link>
          </div>
          <div className="Header__Right">
            <CitySelect size="middle">
              <BsGeoAltFill />
              <span className="Select__Placeholder__Title">Ваш регион</span>
            </CitySelect>
            {user ? (
              <Link to={'/profile'}>
                <Button type="primary">Мой профиль</Button>
              </Link>
            ) : (
              <Link to={'/login'}>
                <Button type="primary">Войти</Button>
              </Link>
            )}
          </div>
        </div>
      </div>
    </header>
  );
};

export default Header;
