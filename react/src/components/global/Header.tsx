import React, { useEffect, useRef, useState } from 'react';
import { Link } from 'react-router-dom';
import { Button, Select } from 'antd';
import { BsGeoAltFill } from 'react-icons/bs';
import axios from 'axios';

const Header = () => {
  const [cities, setCities] = useState<any[]>([]);

  useEffect(() => {
    axios
      .get('mock/pet_blood_group/1')
      .then((response) => {
        if (response.status === 200 && response.data) {
          setCities(response.data);
        }
      })
      .catch((error) => console.error(error));
  }, []);

  return (
    <header className="Header">
      <div className="container">
        <div className="Header__Wrapper">
          <div className="Header__Left">
          <Link to={"/"}>
            <div className="Header__Logo">
              <img src="images/logo.svg" alt="Donor Search" />
            </div>
            </Link>
            <Link to="/haha">Как стать донором?</Link>
            <Link to="/haha">Как сдать кровь?</Link>
          </div>
          <div className="Header__Right">
            <Select
              showSearch
              onClick={(e) => e?.stopPropagation()}
              placeholder={
                <div className="Select__Placeholder">
                  <BsGeoAltFill />
                  <span className="Select__Placeholder__Title">Ваш регион</span>
                </div>
              }
              optionFilterProp="search"
              options={cities.map((item) => {
                return {
                  label: (
                    <>
                      {item.rhesus_type.title} <span>{item.rhesus_type.title}</span>
                    </>
                  ),
                  value: item.rhesus_type.id,
                  search: item.rhesus_type.title,
                };
              })}
            />
            <Button type="primary">
              <Link to={'/login'}>Войти</Link>{' '}
            </Button>
          </div>
        </div>
      </div>
    </header>
  );
};

export default Header;
