import { Dispatch, SetStateAction, useState } from "react";
import { Input } from "antd";
import { Button } from "antd";

const RecipientForm = () => {
  const [reason, setReason] = useState("");
  const [veterinaryСlinic, setVeterinaryСlinic] = useState("");
  const [bloodAmount, setBloodAmount] = useState("");
  const [deadline, setDeadline] = useState("");

  const handleChange = (
    e: React.ChangeEvent<HTMLInputElement>,
    set: Dispatch<SetStateAction<any>>,
  ) => {
    set(e.target.value);
  };

  return (
    <div>
      <div>Форма реципиента</div>
      <div>
        <Input
          placeholder={"Причина поиска животного-донора"}
          value={reason}
          type="text"
          onChange={(e) => handleChange(e, setReason)}
        />
        <Input
          placeholder={"Ветеринарная клиника"}
          value={veterinaryСlinic}
          type="text"
          onChange={(e) => handleChange(e, setVeterinaryСlinic)}
        />
        <Input
          placeholder={"Количество крови"}
          value={bloodAmount}
          type="number"
          onChange={(e) => handleChange(e, setBloodAmount)}
        />
        <div>Дата, до которой поиск актуален</div>
        <Input
          placeholder={"Дата, до которой поиск актуален"}
          value={deadline}
          type="date"
          onChange={(e) => handleChange(e, setDeadline)}
        />
        <Button>Отправить заявку</Button>
      </div>
    </div>
  );
};

export default RecipientForm;
