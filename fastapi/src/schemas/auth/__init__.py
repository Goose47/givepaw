from pydantic import BaseModel
from typing import Optional


class RegisterUser(BaseModel):
    username: str

    name: str
    surname: str
    patronymic: str

    email: str
    password: str

    user_role_id: int
    city_id: int
    avatar_id: Optional[int]


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
