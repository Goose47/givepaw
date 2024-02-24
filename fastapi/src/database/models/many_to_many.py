import datetime

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.database.models import Base
import src.schemas.responds as schemas
from src.schemas.clinics import create_clinic
from src.schemas.donors import create_donor
from src.schemas.recipients import create_recipient


class PetVaccination(Base):
    __tablename__ = "pet__vaccinations"
    extend_existing = True

    pet_id: Mapped[int] = mapped_column(ForeignKey("pets.id"), nullable=False, primary_key=True)
    vaccination_id: Mapped[int] = mapped_column(ForeignKey("vaccinations.id"), nullable=False, primary_key=True)
    vaccination_date: Mapped[datetime.date] = mapped_column(nullable=False)
    # document: Mapped[str] = mapped_column(nullable=True)


class DonorRecipient(Base):
    __tablename__ = "donors__recipient"

    donor_id: Mapped[int] = mapped_column(ForeignKey("donors.id"), nullable=False, primary_key=True)
    donor: Mapped["Donor"] = relationship(lazy="selectin", uselist=False)

    recipient_id: Mapped[int] = mapped_column(ForeignKey("recipient.id"), primary_key=True, nullable=False)
    recipient: Mapped["Recipient"] = relationship(lazy="selectin", uselist=False)

    clinic_id: Mapped[int] = mapped_column(ForeignKey("clinics.id"), nullable=False)
    clinic: Mapped["Clinic"] = relationship(uselist=False, lazy="selectin")

    date: Mapped[datetime.date] = mapped_column(nullable=False)
    blood_amount: Mapped[float] = mapped_column(nullable=False, default=0)
    # status:


def create_donor_recipient(donor_recipient: DonorRecipient):
    return schemas.DonorRecipient(
        donor=create_donor(donor_recipient.donor),
        recipient=create_recipient(donor_recipient.recipient),
        clinic=create_clinic(donor_recipient.clinic),
        date=donor_recipient.date,
        blood_amount=donor_recipient.blood_amount
    )
