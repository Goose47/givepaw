from src.schemas.base import BaseResponseSchema
from src.schemas.characteristics.base import BaseCharacteristic


class UserRole(BaseCharacteristic):
    pass


class UserRoleResponse(UserRole, BaseResponseSchema):
    pass


class UserRoleCreate(UserRole):
    pass


class UserRoleUpdate(UserRole):
    pass
