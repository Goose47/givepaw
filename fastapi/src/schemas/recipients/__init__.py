from pydantic import BaseModel
import datetime


class RecipientViewType(BaseModel):
    id: int

    reason: str
    blood_component_id: int
    blood_amount: int
    donor_amount: int
    pet_id: int
    clinic_id: int
    end_actual_date: datetime.date


class RecipientCreateType(BaseModel):
    reason: str
    blood_component_id: int
    blood_amount: int
    donor_amount: int
    pet_id: int
    clinic_id: int
    end_actual_date: datetime.date
