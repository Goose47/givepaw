import React, { Dispatch, SetStateAction, useEffect, useState } from "react";
import { useNavigate, useParams } from "react-router-dom";
import axios from "axios";
import Radio from "antd/es/radio";
import { Button, Input, notification, Select } from "antd";
import DateSelector from "../components/global/DateSelector";

interface BloodComponent {
  "id": 0,
  "title": "string"
}

interface Clinic {
  "id": 0,
  "title": "string",
  "address": "string",
  "email": "string",
  "phone": "string",
  "city": {
    "id": 0,
    "title": "string",
    "region": {
      "id": 0,
      "title": "string"
    }
  }
}

const RecipientForm = () => {

  const navigate = useNavigate()
  const [bloods, setBloods] = useState<BloodComponent[]>([])
  const [clinics, setClinics] = useState<Clinic[]>([])
  const [blood, setBlood] = useState<number>()
  const [clinic, setClinic] = useState<number>()
  const [date, setDate] = useState<string>()

  const [countPeople, setCountPeople] = useState<string>()
  const [countML, setCountML] = useState<string>()
  const [reason, setReason] = useState<string>()


  useEffect(() => {
    axios.get('pets/blood_components').then(response => {
      setBloods(response.data)
    })
    axios.get('clinics/').then(response => {
      setClinics(response.data)
    })
  }, []);

  const handleChangeBloodComponent = (value : any) => {
    setBlood(value.target.value)
  }

  const handleSelectClinic = (value: any) => {
    setClinic(value)
  }

  const handleChangeDate = (value: string) => {
    setDate(value)
  }

  const { id } = useParams()

  const [api, contextHolder] = notification.useNotification();
  const openNotificationWithIcon = () => {
    api["success"]({
      message: 'Размещено на сайте!',
      description:
        'Спасибо за оставленную заявку. В ближайшее время с вами свяжется менеджер через социальные сети, указанные в профиле.',
    });
  };

  const handleDonorCreate = () => {
    axios.post('recipients/', {
      "reason": reason,
      "blood_component_id": blood,
      "blood_amount": countML,
      "donor_amount": countPeople,
      "pet_id": id,
      "clinic_id": clinic,
      "end_actual_date": date
    }).then(response => {
      openNotificationWithIcon()
      setTimeout(() => {
        navigate('/')
      }, 3000)
    }).catch(error => {
      if (error.response.status === 400) {
        alert(error.response.data.detail)
      }
    })
  }

  const handleChange = (e: React.ChangeEvent<HTMLInputElement>, set: Dispatch<SetStateAction<any>>) => {
    set(e.target.value);
  };

  return (
    <div className="Form">
      <h1>Форма реципиента</h1>
      {contextHolder}

      <div className="Form__Item">
        <div>Компонент крови</div>
        {bloods && (
          <div className="Form__Element">
            <Radio.Group size="large" onChange={handleChangeBloodComponent} defaultValue="a">
              {bloods.map((component) => (
                <Radio.Button key={component.id} value={component.id}>
                  {component.title}
                </Radio.Button>
              ))}
            </Radio.Group>
          </div>
        )}
      </div>

      <div className="Form__Item Form__Clinic">
        <div>Выберите клинику, в которой вы можете принимать кровь</div>
        {clinics && (
          <Select
            size="large"
            showSearch
            onClick={(e) => e?.stopPropagation()}
            onChange={handleSelectClinic}
            placeholder="Выберите клинику"
            optionFilterProp="search"
            options={clinics.map((item) => {
              return {
                label: (
                  <>
                    {item.title} {' '}
                    <span>{item.city?.title}</span>
                  </>
                ),
                value: item.id,
                search: item.title + ', ' + item.city?.title,
              };
            })}
          />
        )}
      </div>

      <div className="Form__Item">
        <div>Когда крайний срок сдачи крови?</div>
        <DateSelector onChange={handleChangeDate} />
      </div>

      <label htmlFor="reason">Введите причину сбора крови для питомца</label>
      <Input
        id="reason"
        size="large"
        placeholder={'Причина сбора крови'}
        value={reason}
        type="text"
        onChange={(e) => handleChange(e, setReason)}
      />

      <label htmlFor="countML">Количество необходимой крови (мл)</label>
      <Input
        id="countML"
        size="large"
        placeholder={'150'}
        value={countML}
        type="text"
        onChange={(e) => handleChange(e, setCountML)}
      />

      <label htmlFor="countPeople">Предполагаемое количество доноров</label>
      <Input
        id="countPeople"
        size="large"
        placeholder={'7'}
        value={countPeople}
        type="text"
        onChange={(e) => handleChange(e, setCountPeople)}
      />

      <Button style={{ marginTop: 30 }} size="large" type="primary" onClick={handleDonorCreate}>Создать</Button>

    </div>
  )
}

export default RecipientForm;
