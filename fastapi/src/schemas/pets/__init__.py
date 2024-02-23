from pydantic import BaseModel


class PetViewType(BaseModel):
    id: int

    blood_group_id: int
    breed_id: int
    breed: str
    pet_type_id: int
    avatar_id: int
    name: str
    age: int
    weight: float
    user_id: int
