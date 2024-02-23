from src.schemas.base import BaseResponseSchema
from src.schemas.characteristics.base import BaseCharacteristic


class UserStatus(BaseCharacteristic):
    is_available: bool


class UserStatusResponse(UserStatus, BaseResponseSchema):
    pass


class UserStatusCreate(UserStatus):
    pass


class UserStatusUpdate(UserStatus):
    pass
