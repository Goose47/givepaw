import React, { useState } from 'react';
import RecipientItem from './RecipientItem';
import { Link } from 'react-router-dom';
import { FaArrowRight } from 'react-icons/fa6';
import { Recipient } from '../Home/HomeRecipientsLibrary';
import PetSelect from '../Forms/PetSelect';

const RecipientsLibrary = () => {
  const [recipients, setRecipients] = useState<Recipient[]>([]);
  const [petType, setPetType] = useState<number>();

  return (
    <div className="RecipientsLibrary">
      <h1>Потребность в донорах</h1>
      <div className="RecipientsLibrary__Filters">
        <div className="RecipientsLibrary__Filter">
          <PetSelect onChange={setPetType} />
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
  );
};

export default RecipientsLibrary;
