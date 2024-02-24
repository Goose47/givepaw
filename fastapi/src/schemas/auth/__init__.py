from pydantic import BaseModel
from typing import Optional
from pydantic import EmailStr, Field
from fastapi import Form, UploadFile


class RegisterUser(BaseModel):
    username: str

    name: str
    surname: str
    patronymic: str

    email: EmailStr = Field()
    password: str

    city_id: int
    # user_role_id: Optional[int] = None
    # todo avatar

    @classmethod
    def as_form(
            cls,
            username: str = Form(),
            name: str = Form(),
            surname: str = Form(),
            patronymic: str = Form(),
            email: EmailStr = Form(),
            password: str = Form(),
            city_id: int = Form(),
            # user_role_id: int = Form(),
    ):
        return cls(
            username=username,
            name=name,
            surname=surname,
            patronymic=patronymic,
            email=email,
            password=password,
            city_id=city_id,
            # user_role_id=user_role_id,
        )


class UserType(BaseModel):
    id: int
    username: str

    name: str
    surname: str
    patronymic: str

    email: str

    user_role_id: int
    city_id: int
    avatar_id: Optional[int]


class LoginUser(BaseModel):
    username: str
    password: str
