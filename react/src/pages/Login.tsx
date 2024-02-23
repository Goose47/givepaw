import React, { Dispatch, SetStateAction, useState } from "react";
import axios from "axios";
import { Button } from "antd";
import { Input } from "antd";

const Login = () => {
  const [login, setLogin] = useState<string>("");
  const [password, setPassword] = useState<string>("");

  const handleChange = (
    e: React.ChangeEvent<HTMLInputElement>,
    set: Dispatch<SetStateAction<any>>,
  ) => {
    set(e.target.value);
  };

  const handleLogin = () => {};

  const handleLogout = () => {};

  return (
    <>
      <div>
        <Input
          placeholder={"Номер телефона или Email"}
          value={login}
          type="text"
          onChange={(e) => handleChange(e, setLogin)}
        />
        <Input
          placeholder={"Пароль"}
          value={password}
          type="text"
          onChange={(e) => handleChange(e, setPassword)}
        />
        <Button>Войти</Button>
      </div>
    </>
  );
};

export default Login;
