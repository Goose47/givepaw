from pydantic import BaseModel


class DonorCreate(BaseModel):
    pet_id: int
    city_id: int


class Donor(BaseModel):
    id: int
    pet_id: int
    city_id: int
