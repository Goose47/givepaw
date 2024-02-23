import { useState } from "react";
import Field from "../components/global/dropdown/Field";

const DonorForm = () => {
  const [animalType, setAnimalType] = useState("");
  const [breed, setBreed] = useState("");
  const [bloodGroup, setBloodGroup] = useState("");
  const [petName, setPetName] = useState("");
  const [image, setImage] = useState(undefined);
  const [age, setAge] = useState("");
  const [weight, setWeight] = useState("");
  const [vaccinations, setVaccinations] = useState([]);

  return (
    <div>
      <div>Форма донора</div>
      <div>
        <Field
          label={"Тип животного"}
          id={"animalType"}
          type="text"
          value={animalType}
          setValue={setAnimalType}
        />
        <Field
          label={"Порода"}
          id={"breed"}
          type="text"
          value={breed}
          setValue={setBreed}
        />
        <Field
          label={"Группа крови"}
          id={"bloodGroup"}
          type="number"
          value={bloodGroup}
          setValue={setBloodGroup}
        />
        <div>Загрузите фото животного</div>
        <input type="file" accept="image/png, image/jpeg"></input>
        <Field
          label={"Кличка"}
          id={"petName"}
          type="text"
          value={petName}
          setValue={setPetName}
        />
        <Field
          label={"Возраст"}
          id={"age"}
          type="number"
          value={age}
          setValue={setAge}
        />
        <Field
          label={"Вес"}
          id={"weight"}
          type="number"
          value={weight}
          setValue={setWeight}
        />
        {/* <Field label={"Прививки"} id={"vaccinations"} value={vaccinations} setValue={setVaccinations}/> */}

        <button>Отправить заявку</button>
      </div>
    </div>
  );
};

export default DonorForm;
