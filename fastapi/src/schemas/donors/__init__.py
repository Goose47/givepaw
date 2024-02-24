from pydantic import BaseModel

from src.schemas.location import City
from src.schemas.pet import Pet


class DonorCreate(BaseModel):
    pet_id: int
    city_id: int


class Donor(BaseModel):
    id: int
    pet: Pet
    city_id: City

