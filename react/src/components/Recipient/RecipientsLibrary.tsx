import React, { useEffect, useState } from "react";
import RecipientItem from "./RecipientItem";
import { Recipient } from "../Home/HomeRecipientsLibrary";
import PetSelect from "../Forms/PetSelect";
import axios from "axios";

const RecipientsLibrary = () => {
  const [recipients, setRecipients] = useState<Recipient[]>([]);
  const [petType, setPetType] = useState<number>();

  useEffect(() => {
    axios
      .post("/recipients/sort_by_data", {})
      .then((response) => {
        setRecipients(response.data);
      });
  }, []);

  return (
    <div className="RecipientsLibrary">
      <h1>Потребность в донорах</h1>
      <div className="RecipientsLibrary__Global">
        <div className="RecipientsLibrary__Filters">
          <h3>Фильтры</h3>
          <div className="RecipientsLibrary__Filter">
            <label htmlFor="pet-select">Вид животного</label>
            <PetSelect id="pet-select" onChange={setPetType} />
          </div>
        </div>
        <div className="RecipientsLibrary__Items">
          <div className="RecipientsLibrary__Wrapper">
            <div className="RecipientsLibrary__Row">
              {recipients.map((recipient) => (
                <div className="RecipientsLibrary__Item">
                  <RecipientItem recipient={recipient} />
                </div>
              ))}
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};

export default RecipientsLibrary;
