import React from 'react';
import { Recipient } from '../Home/HomeRecipientsLibrary';
import { Button, Tag } from 'antd';
import { BsCalendar2DateFill, BsGeoAltFill } from 'react-icons/bs';
import { Link } from 'react-router-dom';

interface RecipientProps {
  recipient: Recipient;
}

const RecipientItem = (props: RecipientProps) => {
  let recipient = props.recipient;

  return (
    <div className="RecipientItem">
      <div className="RecipientItem__Wrapper">
        <div className="RecipientItem__Content">
          <div className="RecipientItem__Header">
            <div className="RecipientItem__Avatar">
              <img src={"https://dev.api.uvuv643.ru/files/avatars/" + recipient.avatar} alt="#" />
            </div>
            <div className="RecipientItem__Title">
              {recipient.name}
              <span>
                <BsCalendar2DateFill /> {recipient.deadline.toLowerCase()}
              </span>
            </div>
          </div>
          <div className="RecipientItem__Place">
            <BsGeoAltFill /> {recipient.place}
          </div>
          <div>Необходимо доноров: {recipient.number_required}</div>
          <div>
            Группа крови: <Tag>{recipient.blood_group}</Tag>
          </div>
          <div>{recipient.reason}</div>
        </div>
        <div className="RecipientItem__Footer">
          <Link
            to="/respond-form"
            state={{
              bloodGroup: recipient.blood_group,
              id: recipient.id,
              place: recipient.place,
              deadline: recipient.deadline,
            }}
          >
            <Button type="primary">Откликнуться</Button>
          </Link>
        </div>
      </div>
    </div>
  );
};

export default RecipientItem;
