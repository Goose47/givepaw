from typing import Optional

from pydantic import BaseModel
import datetime

from src.schemas.blood_group import BloodComponent, create_blood_component
from src.schemas.clinics import Clinic, create_clinic
from src.schemas.pets import Pet, create_pet


class UserNetwork(BaseModel):
    id: int
    telegram: Optional[str] = None
    vk: Optional[str] = None
class UserNetworkCreate(BaseModel):
    id: int
    telegram: Optional[str] = None
    vk: Optional[str] = None
    user_id: Optional[int] = None
class UserNetworkUpdate(BaseModel):
    id: int
    telegram: Optional[str] = None
    vk: Optional[str] = None


def create_user_network(un):
    return UserNetwork(
        id=un.id,
        telegram=un.telegram,
        vk=un.vk,
    )

