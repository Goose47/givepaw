from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from src.database.models import Base


class PetVaccination(Base):
    __table__ = "pet_vaccinations"

    pet_type_id: Mapped[int] = mapped_column(ForeignKey("pet_types.id"), nullable=False)
    vaccination_id: Mapped[int] = mapped_column(ForeignKey("vaccinations.id"), nullable=False)
