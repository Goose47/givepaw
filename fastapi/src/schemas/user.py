from pydantic import BaseModel

from src.schemas.location import City


class UserRole(BaseModel):
    id: int
    title: str


class Avatar(BaseModel):
    id: int
    photo_path: str
    photo_thumb: str


class UserNetwork(BaseModel):
    id: int
    telegram: str
    vk: str


class UserConfig(BaseModel):
    id: int
    phone_number_status: int
    social_networks_status: int
    email_status: int


class UserProfile(BaseModel):
    id: int
    surname: str
    name: str
    patronymic: str
    username: str
    email: str
    user_role: UserRole
    city: City
    avatar: Avatar
    user_network: UserNetwork
    user_config: UserConfig
