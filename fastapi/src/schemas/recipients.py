from typing import Optional

from pydantic import BaseModel
import datetime

from src.schemas.blood_group import BloodComponent, create_blood_component
from src.schemas.clinics import Clinic, create_clinic
from src.schemas.pets import Pet, create_pet


class Recipient(BaseModel):
    id: int

    reason: str
    blood_component: BloodComponent
    blood_amount: int
    donor_amount: int
    pet: Pet
    clinic: Clinic
    end_actual_date: datetime.date


def create_recipient(recipient):
    return Recipient(id=recipient.id, reason=recipient.reason,
                     blood_component=create_blood_component(recipient.blood_component),
                     blood_amount=recipient.blood_amount,
                     donor_amount=recipient.donor_amount, pet=create_pet(recipient.pet),
                     clinic=create_clinic(recipient.clinic),
                     end_actual_date=recipient.end_actual_date)


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
    number_required: int


class RecipientFilter(BaseModel):
    animal_type: Optional[int] = None
    breed: Optional[int] = None
    city: Optional[int] = None
    offset: Optional[int] = None
