from typing import Optional

from pydantic import BaseModel

from src.schemas.location import City


class UserRole(BaseModel):
    id: int
    title: str


class Avatar(BaseModel):
    id: int
    photo_path: str
    photo_thumb: str


def create_avatar(avatar):
    if avatar:
        return Avatar(id=avatar.id, photo_path=avatar.photo_path, photo_thumb=avatar.photo_thumb)
    return avatar


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
    avatar: Optional[Avatar]
    user_network: UserNetwork
    user_config: UserConfig

def create_user(user):
    user = UserProfile(id=user.id, surname=user.surname, name=)

class UserConfigViewType(BaseModel):
    id: int
    phone_number_status: int = 1
    social_networks_status: int = 1
    email_status: int = 1

    user_id: int


class UserConfigCreateType(BaseModel):
    phone_number_status: int = 1
    social_networks_status: int = 1
    email_status: int = 1

    user_id: int


class UserNetworksViewType(BaseModel):
    id: int
    telegram: Optional[str] = None
    vk: Optional[str] = None

    user_id: int


class UserNetworksCreateType(BaseModel):
    telegram: Optional[str] = None
    vk: Optional[str] = None

    user_id: int
