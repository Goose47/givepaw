import React from 'react';
import { Link } from 'react-router-dom';
import { Button } from 'antd';
import { BsGeoAltFill } from 'react-icons/bs';
import CitySelect from './CitySelect';

const Header = () => {
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
            <Link to={'/login'}>
              <Button type="primary">Войти</Button>
            </Link>
          </div>
        </div>
      </div>
    </header>
  );
};

export default Header;
