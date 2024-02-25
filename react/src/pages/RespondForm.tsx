import React, { useEffect, useState } from "react";
import { useLocation, useNavigate, useParams } from "react-router-dom";
import axios from "axios";
import { Button, notification, Select } from "antd";
import DateSelector from "../components/global/DateSelector";
import { BloodComponent, Clinic } from "./DonorForm";
import PetItem, { Pet } from "../components/global/PetItem";
import { Recipient } from "../components/Home/HomeRecipientsLibrary";

const RespondForm = () => {
  const location = useLocation();
  const { pet, id } = useParams();

  const [currentRecipient, setCurrentRecipient] = useState<any>()

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
    axios.get('recipients/' + id).then(response => {
      setCurrentRecipient(response.data)
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

  const [api, contextHolder] = notification.useNotification();
  const openNotificationWithIcon = () => {
    api["success"]({
      message: 'Успешно создано!',
      description:
        'Спасибо за оставленную заявку. В ближайшее время с вами свяжется менеджер через социальные сети, указанные в профиле',
    });
  };

  const handleDonorCreate = () => {
    if (currentRecipient) {
      axios.post('donors/', {
        'clinic_id': currentRecipient.clinic.id,
        'pet_id': pet,
        'recipient_id': id,
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

  }

  return (
    <div className="Form">
      <h1>Срочный сбор крови</h1>

      { currentRecipient && <PetItem pet={currentRecipient.pet} /> }

      {contextHolder}

      <div className="Form__Item">
        <div>Когда вам удобно прийти?</div>
        <DateSelector onChange={handleChangeDate} />
      </div>

      <Button style={{marginTop: 30}} size="large" type="primary" onClick={handleDonorCreate}>Создать</Button>

    </div>
  )

};

export default RespondForm;
