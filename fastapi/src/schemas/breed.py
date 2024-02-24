from pydantic import BaseModel


class BreedResponse(BaseModel):
    id: int
    title: str


class Breed(BaseModel):
    id: int
    title: str
    pet_type_id: int


def create_breed(breed):
    return BreedResponse(id=breed.id, title=breed.title)
