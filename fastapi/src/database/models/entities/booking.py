import datetime
from typing import Optional
from fastapi import Request
from sqlalchemy import ForeignKey
from sqlalchemy.orm import mapped_column, Mapped, relationship

from src.database.models.entities.base import AbstractBaseEntityModelTime


class Booking(AbstractBaseEntityModelTime):
    __tablename__ = "booking"

    advertisement_id: Mapped[int] = mapped_column(ForeignKey("advertisement.id"), nullable=False)
    advertisement: Mapped["Advertisement"] = relationship(back_populates="bookings", uselist=False, lazy="selectin")

    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"), nullable=False)
    user: Mapped["User"] = relationship(back_populates="bookings", uselist=False, lazy="selectin")

    time_from: Mapped[datetime.datetime] = mapped_column(nullable=False)
    time_end: Mapped[datetime.datetime] = mapped_column(nullable=False)

    booking_status_id: Mapped[int] = mapped_column(ForeignKey("booking_status.id"),
                                                   nullable=False)
    booking_status: Mapped["BookingStatus"] = relationship(back_populates="bookings", uselist=False, lazy="selectin")

    guest_count: Mapped[Optional[int]] = mapped_column()

    deadline_at: Mapped[datetime.datetime] = mapped_column(nullable=False)

    def __repr__(self) -> str:
        return (f"Booking(id={self.id}, advertisement_id={self.advertisement_id}, user_id={self.user_id},"
                f"time_from={self.time_from}, time_end={self.time_end}, booking_status_id={self.booking_status_id},"
                f"guest_count={self.guest_count}, deadline_at={self.deadline_at})")

    # [{
    #   from: 12.01.2024 12:00,
    #   to: 16.01.2024 15:00
    # }, { ... }]

    async def __admin_repr__(self, request: Request):
        return f"{self.last_name} {self.first_name}, {self.email}"

    async def __admin_select2_repr__(self, request: Request) -> str:
        return f'<div><span>{self.last_name} {self.first_name}, <i>{self.email}</i></span></div>'
