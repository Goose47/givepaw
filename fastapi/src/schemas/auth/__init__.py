from pydantic import BaseModel
from typing import Optional


class RegisterUser(BaseModel):
    name: str
    surname: str
    patronymic: str
    username: str
    email: str
    password: str

    user_role_id: int
    # google
    # vk
    # tg

    city_id: int
    avatar_id: Optional[int]


class LoginUser(BaseModel):
    username: str
    password: str
