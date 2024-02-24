import React, { useEffect, useState } from "react";
import RecipientItem from "./RecipientItem";
import { Recipient } from "../Home/HomeRecipientsLibrary";
import PetSelect from "../Forms/PetSelect";
import axios from "axios";
import BreedSelect from "../Forms/BreedSelect";
import CitySelect from "../global/CitySelect";
import { Spin } from "antd";


const RecipientsLibrary = () => {
  const [recipients, setRecipients] = useState<Recipient[]>([]);
  const [petType, setPetType] = useState<number>();
  const [city, setCity] = useState<number>();
  const [petBreed, setPetBreed] = useState<number>();

  const [loading, setLoading] = useState<boolean>(false);

  useEffect(() => {
    setLoading(true);
    console.log({
      animal_type: petType,
      breed: petBreed,
      city: city
    });
    axios.post("/recipients/sort_by_data", {
      animal_type: petType,
      breed: petBreed,
      city: city
    }).then((response) => {
      setTimeout(() => {
        setRecipients(response.data);
        setLoading(false);
      }, 500);
    });
  }, [petType, city, petBreed]);


  return (
    <div className="RecipientsLibrary">
      <h1>Потребность в донорах</h1>
      <div className="RecipientsLibrary__Global">
        <div className="RecipientsLibrary__Filters">
          <h3>Фильтры</h3>
          <div className="RecipientsLibrary__Filter">
            <label htmlFor="pet-select">Город</label>
            <CitySelect size="large" onChange={(value: number) => setCity(value)}>
              Ваш город
            </CitySelect>
          </div>
          <div className="RecipientsLibrary__Filter">
            <label htmlFor="pet-select">Вид животного</label>
            <PetSelect id="pet-select" onChange={(value) => {setPetType(value); setPetBreed(undefined)}} />
          </div>
          {
            petType && (
              <div className="RecipientsLibrary__Filter">
                <label htmlFor="breed-select">Порода животного</label>
                <BreedSelect id="breed-select" value={petBreed} onChange={setPetBreed} petType={petType} />
              </div>
            )
          }
        </div>
        <div className="RecipientsLibrary__Items">
          {
            loading ? (
              <div className="Spinner">
                <Spin size={"large"} />
              </div>
            ) : (
              recipients.length ? (
                <div className="RecipientsLibrary__Wrapper">
                  <div className="RecipientsLibrary__Row">
                    {recipients.map((recipient) => (
                      <div className="RecipientsLibrary__Item">
                        <RecipientItem recipient={recipient} />
                      </div>
                    ))}
                  </div>
                </div>
              ) : (
                <h3>Реципиентов с заданными параметрами не существует</h3>
              )
            )
          }

        </div>
      </div>
    </div>
  );
};

export default RecipientsLibrary;
