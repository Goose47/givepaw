import datetime

from pydantic import BaseModel

from src.schemas.clinics import Clinic
from src.schemas.donors import Donor
from src.schemas.recipients import Recipient


class DonorRecipient(BaseModel):
    donor: Donor
    recipient: Recipient
    clinic: Clinic
    date: datetime.date
    blood_amount: float
