from pydantic import BaseModel

from src.schemas.pet_type import PetType


class BreedResponse(BaseModel):
    id: int
    title: str
    pet_type: PetType


class Breed(BaseModel):
    id: int
    title: str
    pet_type_id: int
