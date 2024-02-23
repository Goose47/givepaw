from src.schemas.base import BaseResponseSchema
from src.schemas.characteristics.base import BaseCharacteristic


class BookingStatus(BaseCharacteristic):
    pass


class BookingStatusResponse(BookingStatus, BaseResponseSchema):
    pass


class BookingStatusCreate(BookingStatus):
    pass


class BookingStatusUpdate(BookingStatus):
    pass
