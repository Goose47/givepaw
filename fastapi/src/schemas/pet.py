from pydantic import BaseModel

from src.schemas.blood_group_schemas import BloodGroup


class PetType(BaseModel):
    id: int
    title: str
    icon: str


class Pet(BaseModel):
    id:int
    blood_group: BloodGroup



id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True, nullable=False)

    blood_group_id: Mapped[int] = mapped_column(ForeignKey("pet_blood_groups.id"))
    blood_group: Mapped["PetBloodGroup"] = relationship(uselist=False, lazy="selectin")

    breed_id: Mapped[int] = mapped_column(ForeignKey("breeds.id"), nullable=False)
    _breed: Mapped["Breed"] = relationship(uselist=False, lazy="selectin")

    breed: Mapped[str] = mapped_column(String)

    pet_type_id: Mapped[int] = mapped_column(ForeignKey("pet_types.id"))
    pet_type: Mapped["PetType"] = relationship(uselist=False, lazy="selectin")

    avatar_id: Mapped[int] = mapped_column(ForeignKey("avatars.id"), nullable=False)
    avatar: Mapped["Avatar"] = relationship(uselist=False, lazy="selectin")

    name: Mapped[str] = mapped_column(String, nullable=False)
    age: Mapped[int] = mapped_column(Integer, nullable=False)
    weight: Mapped[float] = mapped_column(Float, nullable=False)

    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"), nullable=False)
    user: Mapped["User"] = relationship(uselist=False, lazy="selectin")

    vaccinations: Mapped[List["Vaccination"]] = relationship(uselist=True, lazy="selectin",
                                                             secondary="pet__vaccinations")