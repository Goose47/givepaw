from typing import Optional

from pydantic import BaseModel

from src.schemas.location import City, create_city
from src.schemas.pets import Pet, create_pet
from src.schemas.recipients import Recipient, create_recipient


class DonorCreate(BaseModel):
    pet_id: int
    city_id: int
    recipient_id: Optional[int] = None


class Donor(BaseModel):
    id: int
    pet: Pet
    city: City
    recipient: Optional[Recipient] = None


def create_donor(donor):
    return Donor(id=donor.id, pet=create_pet(donor.pet), city=create_city(donor.city) if donor.city else None,
                 recipient=create_recipient(donor.recipient) if donor.recipient else None)
