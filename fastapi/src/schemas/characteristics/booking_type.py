from src.schemas.base import BaseResponseSchema
from src.schemas.characteristics.base import BaseCharacteristic


class BookingType(BaseCharacteristic):
    pass
    # title: paid, not paid, cancelled


class BookingTypeResponse(BookingType, BaseResponseSchema):
    pass


class BookingTypeCreate(BookingType):
    pass


class BookingTypeUpdate(BookingType):
    pass
