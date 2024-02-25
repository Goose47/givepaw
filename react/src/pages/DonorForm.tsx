import React, { useEffect, useState } from "react";
import { useNavigate, useParams } from "react-router-dom";
import axios from "axios";
import Radio from "antd/es/radio";
import { Button, notification, Select } from "antd";
import DateSelector from "../components/global/DateSelector";

export interface BloodComponent {
  "id": 0,
  "title": "string"
}

export interface Clinic {
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

const DonorForm = () => {

  const navigate = useNavigate()
  const [bloods, setBloods] = useState<BloodComponent[]>([])
  const [clinics, setClinics] = useState<Clinic[]>([])
  const [blood, setBlood] = useState<number>()
  const [clinic, setClinic] = useState<number>()
  const [date, setDate] = useState<string>()

  useEffect(() => {
    // axios.get('pets/blood_components').then(response => {
    //   setBloods(response.data)
    // })
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
      message: 'Успешно создано!',
      description:
        'Спасибо за оставленную заявку. В ближайшее время с вами свяжется менеджер через социальные сети, указанные в профиле',
    });
  };

  const handleDonorCreate = () => {
    axios.post('donors/', {
      'clinic_id': clinic,
      'pet_id': id,
      'recipient_id': null,
      'date': date
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

  return (
    <div className="Form">
      <h1>Форма донора</h1>
      {contextHolder}
      {/*<div className="Form__Item">*/}
      {/*  <div>Компонент крови</div>*/}
      {/*  {bloods && (*/}
      {/*    <div className="Form__Element">*/}
      {/*      <Radio.Group size="large" onChange={handleChangeBloodComponent} defaultValue="a">*/}
      {/*        {bloods.map((component) => (*/}
      {/*          <Radio.Button key={component.id} value={component.id}>*/}
      {/*            {component.title}*/}
      {/*          </Radio.Button>*/}
      {/*        ))}*/}
      {/*      </Radio.Group>*/}
      {/*    </div>*/}
      {/*  )}*/}
      {/*</div>*/}

      <div className="Form__Item Form__Clinic">
        <div>Выберите клинику, в которой вам удобно сдать кровь</div>
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
        <div>Когда вам удобно прийти?</div>
        <DateSelector onChange={handleChangeDate} />
      </div>

      <Button style={{marginTop: 30}} size="large" type="primary" onClick={handleDonorCreate}>Создать</Button>

    </div>
  )
}

export default DonorForm;
