from src.database.models.characteristics.base import AbstractCharacteristicModel


class BookingType(AbstractCharacteristicModel):
    TYPE_1 = 1
    TYPE_2 = 2
    TYPE_3 = 3

    __tablename__ = "booking_type"

    # TODO: Найти, где использовали. Дописать relationship
    # bookings: Mapped[List["Booking"]] = relationship(back_populates="booking_type", uselist=True, lazy="selectin")

    def __repr__(self) -> str:
        return f"BookingType(id={self.id}, title={self.title})"
