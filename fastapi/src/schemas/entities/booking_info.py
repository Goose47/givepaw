from src.schemas import BaseResponseSchema

from src.schemas.entities.base import BaseEntity


class BookingInfo(BaseEntity):
    field: str


class BookingInfoResponse(BookingInfo, BaseResponseSchema):
    pass


class BookingInfoCreate(BookingInfo):
    pass


class BookingInfoUpdate(BookingInfo):
    pass
