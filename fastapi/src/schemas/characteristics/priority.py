from src.schemas.base import BaseResponseSchema
from src.schemas.characteristics.base import BaseCharacteristic


class Priority(BaseCharacteristic):
    priority: int


class PriorityResponse(Priority, BaseResponseSchema):
    pass
