from pydantic import BaseModel
from typing import Optional


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
