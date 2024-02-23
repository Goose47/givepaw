from typing import List

from sqlalchemy.orm import relationship, Mapped

from src.database.models.characteristics.base import AbstractCharacteristicModel


class BookingStatus(AbstractCharacteristicModel):
    PAID = 1
    NOT_PAID = 2

    __tablename__ = "booking_status"

    bookings: Mapped[List["Booking"]] = relationship(back_populates="booking_status", uselist=True, lazy="selectin")

    def __repr__(self) -> str:
        return f"BookingStatus(id={self.id}, title={self.title})"
