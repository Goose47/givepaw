import React, { useEffect, useRef, useState } from 'react';
import { Link } from 'react-router-dom';
import { Button, Select } from 'antd';
import { BsGeoAltFill } from 'react-icons/bs';
import axios from 'axios';

const Header = () => {
  const [cities, setCities] = useState<any[]>([]);

  const [selectedCity, setSelectedCity] = useState<boolean>(false);

  useEffect(() => {
    axios
      .get('cities/')
      .then((response) => {
        if (response.status === 200 && response.data) {
          setCities(response.data);
        }
      })
      .catch((error) => console.error(error));
  }, []);

  const handleSelectCity = (id: any) => {
    let targetCities = cities.filter((city) => city.id == id);
    if (targetCities.length) {
      let targetCity = targetCities[0];
      localStorage.setItem('city', targetCity.title);
      localStorage.setItem('cityId', targetCity.id);
      localStorage.setItem('region', targetCity.region.title);
      setSelectedCity(true);
    }
  };

  useEffect(() => {
    setSelectedCity(!!localStorage.getItem('city') && !!localStorage.getItem('region'));
  }, []);

  const handleShowSelect = () => {
    setSelectedCity(false);
  };

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
            {selectedCity ? (
              <span onClick={handleShowSelect} className="Header__Region--Selected">
                <BsGeoAltFill />
                {localStorage.getItem('city')}
              </span>
            ) : (
              <>
                <Select
                  showSearch
                  onClick={(e) => e?.stopPropagation()}
                  onChange={handleSelectCity}
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
                          {item.title} <span>{item.region?.title}</span>
                        </>
                      ),
                      value: item.id,
                      search: item.title + ' ' + item.region?.title,
                    };
                  })}
                />
              </>
            )}
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
