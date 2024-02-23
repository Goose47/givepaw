import datetime
from src.schemas import BaseResponseSchema
from src.schemas.entities.base import BaseEntity


class AdBookingAvailable(BaseEntity):
    advertisement_id: int

    time_from: datetime.datetime
    time_end: datetime.datetime

    min_booking_time: datetime.datetime
    max_booking_time: datetime.datetime

    price: float


class AdBookingAvailableResponse(AdBookingAvailable, BaseResponseSchema):
    pass


class AdBookingAvailableCreate(AdBookingAvailable):
    pass


class AdBookingAvailableUpdate(AdBookingAvailable):
    pass
