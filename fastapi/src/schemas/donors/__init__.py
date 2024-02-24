from typing import Optional

from pydantic import BaseModel

from src.schemas.location import City
from src.schemas.pets import Pet
from src.schemas.recipients import Recipient


class DonorCreate(BaseModel):
    pet_id: int
    city_id: int


class Donor(BaseModel):
    id: int
    pet: Pet
    city: City
    recipient: Optional[Recipient]

