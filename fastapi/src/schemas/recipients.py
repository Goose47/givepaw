from pydantic import BaseModel
import datetime

from src.schemas.blood_group import BloodComponent
from src.schemas.clinics import Clinic
from src.schemas.pets import Pet


class Recipient(BaseModel):
    id: int

    reason: str
    blood_component: BloodComponent
    blood_amount: int
    donor_amount: int
    pet: Pet
    clinic_id: Clinic
    end_actual_date: datetime.date


class RecipientCreate(BaseModel):
    reason: str
    blood_component_id: int
    blood_amount: int
    donor_amount: int
    pet_id: int
    clinic_id: int
    end_actual_date: datetime.date


class RecipientForSortByData(BaseModel):
    id: int
    avatar: str
    name: str
    blood_group: str
    place: str
    deadline: str
    reason: str
