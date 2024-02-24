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
    avatar: Avatar
    name: str
    age: int
    weight: float
    user: UserProfile
    vaccinations: List[Vaccination]


def create_pet_type(pet_type):
    return PetType(id=pet_type.id, title=pet_type.title, icon=pet_type.icon)


def create_pet(pet):
    pet = Pet(id=pet.id,
              blood_group=create_pet_blood_group(pet.blood_group),
              _breed=create_breed(pet._breed),
              breed=pet.breed,
              pet_type=create_pet_type(pet.pet_type),
              avatar=create_avatar(pet.avatar),
              name=pet.name,
              age=pet.age,
              weight=pet.weight,
              user=create_user(pet.user),
              vaccinations=create_vaccinations(pet.vaccinations)
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
    user_id: int = None
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


class CreatePetModel(BaseModel):
    blood_group_id: int
    breed_id: Optional[int]
    breed: Optional[str] = None
    pet_type_id: int
    avatar_id: Optional[int]
    name: str
    age: int
    weight: float
    user_id: int = None


def create_pet_model(pet):
    return CreatePetModel(blood_group_id=pet.blood_group_id,
                          breed_id=pet.breed_id,
                          breed=pet.breed,
                          pet_type_id=pet.pet_type_id,
                          avatar_id=pet.avatar_id,
                          name=pet.name,
                          age=pet.age,
                          weight=pet.weight,
                          user_id=pet.user_id
                          )


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
