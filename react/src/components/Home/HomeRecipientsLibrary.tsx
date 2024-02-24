import React, { useState } from 'react';
import RecipientItem from '../Recipient/RecipientItem';
import { Link } from 'react-router-dom';
import { FaArrowRight } from 'react-icons/fa6';

export interface Recipient {
  id: number;
  avatar: string;
  name: string;
  blood_group: string;
  place: string;
  numberTaken: number;
  numberRequired: number;
  deadline: string;
  reason: string;
}

const HomeRecipientsLibrary = () => {
  const [recipients, setRecipients] = useState<Recipient[]>([
    {
      id: 1,
      name: 'Cat 1',
      avatar: 'https://http.cat/101',
      blood_group: '4++',
      place: 'Каменоостровский проспект д. 56',
      numberTaken: 4,
      numberRequired: 7,
      deadline: 'до 30 февраля',
      reason: 'lorem ipsum dolor',
    },
    {
      id: 2,
      name: 'Cat 2',
      avatar: 'https://http.cat/403',
      blood_group: '1-',
      place: 'Вяземский пер. 5-7',
      numberTaken: 3,
      numberRequired: 6,
      deadline: 'до 26 февраля',
      reason: 'lorem ipsum dolor',
    },
    {
      id: 1,
      name: 'Cat 1',
      avatar: 'https://http.cat/200',
      blood_group: '4++',
      place: 'Каменоостровский проспект д. 56',
      numberTaken: 4,
      numberRequired: 7,
      deadline: 'до 30 февраля',
      reason: 'lorem ipsum dolor',
    },
    {
      id: 2,
      name: 'Cat 2',
      avatar: 'https://http.cat/502',
      blood_group: '1-',
      place: 'Вяземский пер. 5-7',
      numberTaken: 3,
      numberRequired: 6,
      deadline: 'до 26 февраля',
      reason: 'lorem ipsum dolor',
    },
  ]);

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
