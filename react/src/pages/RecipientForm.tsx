import { useState } from "react";
import Field from "../components/global/dropdown/Field";

const RecipientForm = () => {
  const [reason, setReason] = useState("");
  const [veterinaryСlinic, setVeterinaryСlinic] = useState("");
  const [bloodAmount, setBloodAmount] = useState("");
  const [deadline, setDeadline] = useState("");

  return (
    <div>
      <div>Форма реципиента</div>
      <div>
        <Field
          label={"Причина поиска животного-донора"}
          id={"reason"}
          type="text"
          value={reason}
          setValue={setReason}
        />
        <Field
          label={"Ветеринарная клиника"}
          id={"veterinaryСlinic"}
          type="text"
          value={veterinaryСlinic}
          setValue={setVeterinaryСlinic}
        />
        <Field
          label={"Количество крови"}
          id={"bloodAmount"}
          type="number"
          value={bloodAmount}
          setValue={setBloodAmount}
        />
        <Field
          label={"Дата, до которой поиск актуален"}
          id={"deadline"}
          type="date"
          value={deadline}
          setValue={setDeadline}
        />

        <button>Отправить заявку</button>
      </div>
    </div>
  );
};

export default RecipientForm;
