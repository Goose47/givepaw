from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from src.database.models import Base


class PetVaccination(Base):
    __table__ = "pet__vaccinations"

    pet_id: Mapped[int] = mapped_column(ForeignKey("pets.id"), nullable=False)
    vaccination_id: Mapped[int] = mapped_column(ForeignKey("vaccinations.id"), nullable=False)
