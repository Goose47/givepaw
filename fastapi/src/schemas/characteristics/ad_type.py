from src.schemas.base import BaseResponseSchema
from src.schemas.characteristics.base import BaseCharacteristic


class AdType(BaseCharacteristic):
    pass


class AdTypeResponse(AdType, BaseResponseSchema):
    pass


class AdTypeCreate(AdType):
    pass


class AdTypeUpdate(AdType):
    pass
