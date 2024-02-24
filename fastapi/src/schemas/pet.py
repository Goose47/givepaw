from pydantic import BaseModel

from src.schemas.blood_group_schemas import BloodGroup
from src.schemas.breed import BreedResponse
from src.schemas.user import Avatar


class PetType(BaseModel):
    id: int
    title: str
    icon: str


class Pet(BaseModel):
    id: int
    blood_group: BloodGroup
    breed: BreedResponse
    pet_type: PetType
    avatar: Avatar
    name: str
    age: int
    weight: float
    # user


"""

    name: Mapped[str] = mapped_column(String, nullable=False)
    age: Mapped[int] = mapped_column(Integer, nullable=False)
    weight: Mapped[float] = mapped_column(Float, nullable=False)

    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"), nullable=False)
    user: Mapped["User"] = relationship(uselist=False, lazy="selectin")

    vaccinations: Mapped[List["Vaccination"]] = relationship(uselist=True, lazy="selectin",
                                                             secondary="pet__vaccinations")
                                                             
"""
