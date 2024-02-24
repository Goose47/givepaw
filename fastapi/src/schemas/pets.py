from typing import List

from pydantic import BaseModel

from src.schemas.blood_group import PetBloodGroup
from src.schemas.breed import Breed, create_breed
from src.schemas.user import Avatar, UserProfile, create_avatar
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
    vaccinations: List[Vaccination]


def create_pet_type(pet_type):
    return PetType(id=pet_type.id, title=pet_type.title, icon=pet_type.icon)


def create_pet(pet):
    pet = Pet(id=pet.id, blood_group=pet.blood_group, breed=create_breed(pet.breed),
              pet_type=create_pet_type(pet.pet_type), avatar=create_avatar(pet.avatar),
              name=pet.name, age=pet.age, weight=pet.weight, user=create_user(pet.user))
    return pet
