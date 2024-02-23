import { Dispatch, SetStateAction, useState } from "react";
import { UploadOutlined } from '@ant-design/icons';
import type { UploadProps } from 'antd';
import { Button, message, Upload } from 'antd';
import { Input } from 'antd';

const DonorForm = () => {
  const [animalType, setAnimalType] = useState("");
  const [breed, setBreed] = useState("");
  const [bloodGroup, setBloodGroup] = useState("");
  const [petName, setPetName] = useState("");
  const [image, setImage] = useState(undefined);
  const [age, setAge] = useState("");
  const [weight, setWeight] = useState("");
  const [vaccinations, setVaccinations] = useState([]);

  const props: UploadProps = {
    name: 'file',
    action: 'https://run.mocky.io/v3/435e224c-44fb-4773-9faf-380c5e6a2188',
    headers: {
      authorization: 'authorization-text',
    },
    onChange(info) {
      if (info.file.status !== 'uploading') {
        console.log(info.file, info.fileList);
      }
      if (info.file.status === 'done') {
        message.success(`${info.file.name} file uploaded successfully`);
      } else if (info.file.status === 'error') {
        message.error(`${info.file.name} file upload failed.`);
      }
    },
  };
  
  const handleChange = (e: React.ChangeEvent<HTMLInputElement>, set: Dispatch<SetStateAction<any>>) => {
    set(e.target.value);
}

  
  return (
    <div>
      <div>Форма донора</div>
      <div>
        <Input
          placeholder={"Тип животного"}
          value={animalType}
          type="text"
          onChange={(e) => handleChange(e, setAnimalType)}
        />
        <Input
          placeholder={"Порода"}
          value={breed}
          type="text"
          onChange={(e) => handleChange(e, setBreed)}
        />
        <Input
          placeholder={"Группа крови"}
          value={bloodGroup}
          type="number"
          onChange={(e) => handleChange(e, setBloodGroup)}
        />
        <Input
          placeholder={"Кличка"}
          value={petName}
          type="text"
          onChange={(e) => handleChange(e, setPetName)}
        />
        <Input
          placeholder={"Возраст"}
          value={age}
          type="text"
          onChange={(e) => handleChange(e, setAge)}
        />
        <Input
          placeholder={"Вес"}
          value={weight}
          type="text"
          onChange={(e) => handleChange(e, setWeight)}
        />
        <Upload {...props}>
        <Button icon={<UploadOutlined />}>Загрузите фото животного</Button>
        </Upload>

        {/* <Field label={"Прививки"} id={"vaccinations"} value={vaccinations} setValue={setVaccinations}/> */}

        <Button>Отправить заявку</Button>
      </div>
    </div>
  );
};

export default DonorForm;
