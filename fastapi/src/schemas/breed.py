from pydantic import BaseModel

from src.schemas.pet import PetType


class BreedResponse(BaseModel):
    id: int
    title: str


class Breed(BaseModel):
    id: int
    title: str
    pet_type_id: int
