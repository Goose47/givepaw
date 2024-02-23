import datetime

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from src.database.models import Base


class PetVaccination(Base):
    __tablename__ = "pet__vaccinations"
    extend_existing = True

    pet_id: Mapped[int] = mapped_column(ForeignKey("pets.id"), nullable=False, primary_key=True)
    vaccination_id: Mapped[int] = mapped_column(ForeignKey("vaccinations.id"), nullable=False, primary_key=True)


class DonorRecipient(Base):
    __tablename__ = "donors__recipient"

    donor_id: Mapped[int] = mapped_column(ForeignKey("donors.id"), nullable=False, primary_key=True)
    recipient_id: Mapped[int] = mapped_column(ForeignKey("recipient.id"), nullable=False, primary_key=True)

    date: Mapped[datetime.date] = mapped_column()
    blood_amount: Mapped[float] = mapped_column()
    # status:
