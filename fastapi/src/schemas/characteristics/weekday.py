from typing import ClassVar, Optional, Optional

from src.schemas.base import BaseResponseSchema
from src.schemas.characteristics.base import BaseCharacteristic


class Weekday(BaseCharacteristic):
    short_title: Optional[str]
    order: int


class WeekdayResponse(Weekday, BaseResponseSchema):
    pass


class WeekdayCreate(Weekday):
    pass


class WeekdayUpdate(Weekday):
    pass
