import React, { useEffect, useState } from 'react';
import axios from 'axios';
import { BsGeoAltFill } from 'react-icons/bs';
import { Select } from 'antd';
import { SizeType } from 'antd/es/config-provider/SizeContext';

interface CitySelectProps {
  size: SizeType;
  children: React.ReactNode;
  onChange?: React.ChangeEventHandler<HTMLInputElement>;
}

const CitySelect = (props: CitySelectProps) => {
  const [cities, setCities] = useState<any[]>([]);
  const [selectedCity, setSelectedCity] = useState<boolean>(false);

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

  return (
    <>
      {selectedCity ? (
        <span onClick={handleShowSelect} className="Header__Region--Selected">
          <BsGeoAltFill />
          {localStorage.getItem('city')}
        </span>
      ) : (
        <>
          <Select
            size={props.size}
            showSearch
            onClick={(e) => e?.stopPropagation()}
            onChange={handleSelectCity}
            placeholder={<div className="Select__Placeholder">{props.children}</div>}
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
    </>
  );
};

export default CitySelect;
