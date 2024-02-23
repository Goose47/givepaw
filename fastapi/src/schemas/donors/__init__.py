from pydantic import BaseModel


class DonorCreateType(BaseModel):
    pet_id: int
    city_id: int


class DonorViewType(BaseModel):
    id: int
    pet_id: int
    city_id: int
