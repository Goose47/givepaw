from pydantic import BaseModel

from src.schemas.location import City, create_city


class Clinic(BaseModel):
    id: int
    title: str
    address: str
    email: str
    phone: str
    city: City


def create_clinic(clinic):
    return Clinic(id=clinic.id, title=clinic.title, address=clinic.address, email=clinic.email, phone=clinic.phone,
                  city=create_city(clinic.city))
