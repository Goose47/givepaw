from pydantic import BaseModel

from src.schemas.location import City


class Clinic(BaseModel):
    id: int
    title: str
    address: str
    email: str
    phone: str
    city: City
