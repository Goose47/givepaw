from pydantic import BaseModel
from typing import Optional


class RegisterUser(BaseModel):
    username: str

    name: str
    surname: str
    patronymic: str

    email: str
    password: str

    city_id: int
    user_role_id: Optional[int] = None
    # todo avatar


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
