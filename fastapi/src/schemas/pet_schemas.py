from src.schemas.user import *
from src.schemas.vaccination import *
from pydantic import BaseModel


class RhesusType(BaseModel):
    id: int
    title: str


class BloodGroup(BaseModel):
    id: int
    title: str


class PetBloodGroup(BaseModel):
    id: int
    blood_group: BloodGroup
    rhesus_type: RhesusType


class Breed(BaseModel):
    id: int
    title: str


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
