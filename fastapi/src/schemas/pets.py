from typing import List, Optional

from pydantic import BaseModel
from fastapi import Form

from src.schemas.blood_group import PetBloodGroup, create_pet_blood_group
from src.schemas.breed import Breed, create_breed
from src.schemas.user import Avatar, UserProfile, create_avatar, create_user
from src.schemas.vaccination import Vaccination, create_vaccinations, PetVaccinationCreate


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
    _breed: Optional[Breed]
    breed: Optional[str]
    pet_type: PetType
    name: str
    age: int
    weight: float
    user: UserProfile
    vaccinations: List[Vaccination]
    avatar_link: Optional[str] = None


def create_pet_type(pet_type):
    return PetType(id=pet_type.id, title=pet_type.title, icon=pet_type.icon)


def create_pet(pet):
    pet = Pet(
        id=pet.id,
        blood_group=create_pet_blood_group(pet.blood_group) if pet.blood_group else None,
        _breed=create_breed(pet._breed) if pet._breed else None,
        breed=pet.breed,
        pet_type=create_pet_type(pet.pet_type) if pet.pet_type else None,
        name=pet.name,
        age=pet.age,
        weight=pet.weight,
        user=create_user(pet.user) if pet.user else None,
        vaccinations=create_vaccinations(pet.vaccinations) if pet.vaccinations else None,
        avatar_link=pet.avatar_link,
    )
    return pet


class CreatePet(BaseModel):
    blood_group_id: int
    breed_id: Optional[int]
    breed: Optional[str] = None
    pet_type_id: int
    avatar: Optional[str] = None
    avatar_id: Optional[int] = None
    name: str
    age: int
    weight: float
    user_id: Optional[int] = None
    vaccinations: Optional[List[PetVaccinationCreate]]

    ## as_form не нужен
    @classmethod
    def as_form(
            cls,
            blood_group_id: int = Form(),
            breed_id: Optional[int] = Form(None),
            breed: Optional[str] = Form(None),
            pet_type_id: int = Form(),
            name: str = Form(),
            age: int = Form(),
            weight: float = Form(),
            user_id: int = Form(),
            # vaccinations: list[PetVaccinationCreate] = Form(),
            vaccinations: list = Form(),
    ):
        return cls(
            blood_group_id=blood_group_id,
            breed_id=breed_id,
            breed=breed,
            pet_type_id=pet_type_id,
            name=name,
            age=age,
            weight=weight,
            user_id=user_id,
            vaccinations=vaccinations,
        )


class MyPetResponse(BaseModel):
    id: int
    blood_group_title: str
    breed_title: str
    pet_type_title: str
    avatar_link: Optional[str] = None
    name: str
    age: int
    weight: float
    vaccinations: Optional[List[str]] = None
