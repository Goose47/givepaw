import React from 'react';
import { Recipient } from '../Home/HomeRecipientsLibrary';
import { Button, Tag } from 'antd';
import { BsCalendar2DateFill, BsGeoAltFill } from 'react-icons/bs';

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
              <img src={recipient.avatar} alt="#" />
            </div>
            <div className="RecipientItem__Title">
              {recipient.name}
              <span>
                <BsCalendar2DateFill /> {recipient.deadline}
              </span>
            </div>
          </div>
          <div className="RecipientItem__Place">
            <BsGeoAltFill /> {recipient.place}
          </div>
          <div>Необходимо доноров: {recipient.numberRequired}</div>
          <div>
            Группа крови: <Tag>{recipient.blood_group}</Tag>
          </div>
          <div>{recipient.reason}</div>
        </div>
        <div className="RecipientItem__Footer">
          <Button type="primary">Откликнуться</Button>
        </div>
      </div>
    </div>
  );
};

export default RecipientItem;
