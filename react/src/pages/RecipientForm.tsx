import React, { Dispatch, SetStateAction, useState } from 'react';
import { Input } from 'antd';
import { Button } from 'antd';
import { Link, useNavigate } from 'react-router-dom';

const RecipientForm = () => {
  const [reason, setReason] = useState('');
  const [veterinaryСlinic, setVeterinaryСlinic] = useState('');
  const [bloodAmount, setBloodAmount] = useState('');
  const [bloodComponent, setBloodComponent] = useState('');
  const [donorAmount, setDonorAmount] = useState('');
  const [deadline, setDeadline] = useState('');
  const navigate = useNavigate();

  const handleChange = (e: React.ChangeEvent<HTMLInputElement>, set: Dispatch<SetStateAction<any>>) => {
    set(e.target.value);
  };

  const handleSend = () => {
    // .then(navigate(`/profile`));
  };

  return (
    <div>
      <div className="Form">
        <h1>Форма реципиента</h1>

        <label htmlFor="email">Причина поиска животного-донора</label>
        <Input
          size="large"
          id="email"
          placeholder={'Причина поиска животного-донора'}
          value={reason}
          type="text"
          onChange={(e) => handleChange(e, setReason)}
        />

        <label htmlFor="clinic">Ветеринарная клиника</label>
        <Input
          size="large"
          id="clinic"
          placeholder={'Ветеринарная клиника'}
          value={veterinaryСlinic}
          type="text"
          onChange={(e) => handleChange(e, setVeterinaryСlinic)}
        />

        <label htmlFor="blood-amount">Количество крови (мл)</label>
        <Input
          size="large"
          id="blood-amount"
          placeholder={'Количество крови'}
          value={bloodAmount}
          type="number"
          onChange={(e) => handleChange(e, setBloodAmount)}
        />

        <label htmlFor="deadline">Дата, до которой поиск актуален</label>
        <Input
          size="large"
          id="deadline"
          placeholder={'Дата, до которой поиск актуален'}
          value={deadline}
          type="date"
          onChange={(e) => handleChange(e, setDeadline)}
        />

        <Button type="primary" onClick={handleSend}>
          Отправить заявку
        </Button>
      </div>
    </div>
  );
};

export default RecipientForm;
