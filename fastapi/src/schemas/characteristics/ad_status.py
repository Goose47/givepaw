from typing import ClassVar

from src.schemas.base import BaseResponseSchema
from src.schemas.characteristics.base import BaseCharacteristic


# + not paid
class AdStatus(BaseCharacteristic):
    is_shown: bool


class AdStatusResponse(AdStatus, BaseResponseSchema):
    pass


class AdStatusCreate(AdStatus):
    pass


class AdStatusUpdate(AdStatus):
    pass
