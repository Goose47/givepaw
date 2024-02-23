import datetime
from typing import Optional
from src.schemas import BaseResponseSchema
from src.schemas.entities.base import BaseEntityTime


class Booking(BaseEntityTime):
    advertisement_id: int
    user_id: int

    time_from: datetime.datetime
    time_end: datetime.datetime

    booking_status_id: int

    guest_count: Optional[int]

    deadline_at: datetime.datetime


# [{
#   from: 12.01.2024 12:00,
#   to: 16.01.2024 15:00
# }, { ... }]

class BookingResponse(Booking, BaseResponseSchema):
    pass


class BookingCreate(Booking):
    pass


class BookingUpdate(Booking):
    pass
