from typing import List, Optional

from pydantic import BaseModel

from src.schemas.blood_group import PetBloodGroup, create_pet_blood_group
from src.schemas.breed import Breed, create_breed
from src.schemas.user import Avatar, UserProfile, create_avatar, create_user
from src.schemas.vaccination import Vaccination, create_vaccinations


class PetType(BaseModel):
    id: int
    title: str
    icon: str

    @property
    def link(self):
        return self.icon + 'jajajaja'


class Pet(BaseModel):
    id: int
    blood_group: PetBloodGroup
    _breed: Breed
    breed: str
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
    pet = Pet(id=pet.id, blood_group=create_pet_blood_group(pet.blood_group), _breed=create_breed(pet._breed),
              breed=pet.breed,
              pet_type=create_pet_type(pet.pet_type), avatar=create_avatar(pet.avatar),
              name=pet.name, age=pet.age, weight=pet.weight, user=create_user(pet.user),
              vaccinations=create_vaccinations(pet.vaccinations))
    return pet


"""
class CreatePetRequest(BaseModel):
    blood_group: PetBloodGroup
    breed_id: id
    pet_type_id: int
    avatar_id: int
    name: str
    age: int
    weight: float
    user_id: Optional[int]
    vaccinations: List[Vaccination]

    arbitrary_types_allowed = True

"""


class CreatePet(BaseModel):
    blood_group_id: int
    breed_id: Optional[int]
    breed: Optional[str]
    pet_type_id: int
    avatar_id: Optional[int]
    name: str
    age: int
    weight: float
    user_id: Optional[int]
    vaccinations: Optional[List[Vaccination]]


class MyPetResponse(BaseModel):
    id: int
    blood_group_title: str
    breed_title: str
    pet_type_title: str
    avatar_path: str
    name: str
    age: int
    weight: float
    vaccinations: List[str]
