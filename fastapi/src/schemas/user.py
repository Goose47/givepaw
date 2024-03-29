from typing import Optional

from pydantic import BaseModel

from src.schemas.location import City, create_city


class UserRole(BaseModel):
    id: int
    title: str


def create_user_role(user_role):
    return UserRole(id=user_role.id, title=user_role.title)


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
    telegram: Optional[str]
    vk: Optional[str]


def create_user_network(user_network):
    if user_network:
        return UserNetwork(id=user_network.id, telegram=user_network.telegram, vk=user_network.vk)
    return user_network


class UserConfig(BaseModel):
    id: int
    phone_number_status: int
    social_networks_status: int
    email_status: int


def create_user_config(user_config):
    if user_config:
        return UserConfig(id=user_config.id, phone_number_status=user_config.phone_number_status,
                          social_networks_status=user_config.social_networks_status,
                          email_status=user_config.email_status)
    return user_config


class UserProfile(BaseModel):
    id: int
    surname: str
    name: str
    patronymic: str
    username: str
    email: str
    user_role: UserRole
    city: City
    avatar_link: Optional[str] = None
    user_network: UserNetwork
    user_config: UserConfig


class UserUpdate(BaseModel):
    surname: Optional[str] = None
    name: Optional[str] = None
    patronymic: Optional[str] = None
    username: Optional[str] = None
    email: Optional[str] = None
    city_id: Optional[int] = None


class UserChangePassword(BaseModel):
    password: str


def create_user(user):
    user = UserProfile(id=user.id, surname=user.surname, name=user.name, patronymic=user.patronymic,
                       username=user.username,
                       email=user.email,
                       user_role=create_user_role(user.user_role) if user.user_role else None,
                       city=create_city(user.city) if user.city else None,
                       avatar=create_avatar(user.avatar) if user.avatar else None,
                       user_network=create_user_network(user.user_network) if user.user_network else None,
                       user_config=create_user_config(user.user_config) if user.user_config else None)
    return user


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
