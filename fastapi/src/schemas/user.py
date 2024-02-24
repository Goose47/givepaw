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
    telegram: str
    vk: str


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
                      social_networks_status=user_config.social_networks_status, email=user_config.email_status)
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
    avatar: Optional[Avatar]
    user_network: UserNetwork
    user_config: UserConfig


def create_user(user):
    user = UserProfile(id=user.id, surname=user.surname, name=user.name, patronymic=user.patronymic,
                       username=user.username,
                       email=user.email, user_role=create_user_role(user.user_role), city=create_city(user.city),
                       avatar=create_avatar(user.avatar), user_network=create_user_network(user.user_network),
                       user_config=create_user_config(user.user_config))
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
