import React, { useEffect, useState } from 'react';
import RecipientItem from '../Recipient/RecipientItem';
import { Link } from 'react-router-dom';
import { FaArrowRight } from 'react-icons/fa6';
import axios from 'axios';

export interface Recipient {
  id: number;
  avatar: string;
  name: string;
  blood_group: string;
  place: string;
  number_required: number;
  deadline: string;
  reason: string;
}

const HomeRecipientsLibrary = () => {
  const [recipients, setRecipients] = useState<Recipient[]>([]);

  useEffect(() => {
    axios
      .post('/recipients/sort_by_data', {
        offset: 4,
      })
      .then((response) => {
        setRecipients(response.data);
      });
  }, []);

  return (
    <div className="HomeRecipients">
      <h1>Потребность в донорах</h1>
      <div className="HomeRecipients__Wrapper">
        <div className="HomeRecipients__Row">
          {recipients.map((recipient) => (
            <div className="HomeRecipients__Item">
              <RecipientItem recipient={recipient} />
            </div>
          ))}
        </div>
      </div>
      <Link to="recipients" className="HomeRecipients__Link">
        Узнать больше <FaArrowRight />
      </Link>
    </div>
  );
};

export default HomeRecipientsLibrary;
