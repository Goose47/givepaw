from pydantic import BaseModel

from src.schemas.blood_group import PetBloodGroup
from src.schemas.breed import Breed
from src.schemas.user import Avatar, UserProfile
from src.schemas.vaccination import Vaccination


class PetType(BaseModel):
    id: int
    title: str
    icon: str


class Pet(BaseModel):
    id: int
    blood_group: PetBloodGroup
    breed: Breed
    pet_type: PetType
    avatar: Avatar
    name: str
    age: int
    weight: float
    user: UserProfile
    vaccinations: list[Vaccination]
