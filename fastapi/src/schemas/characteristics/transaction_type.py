from src.schemas.base import BaseResponseSchema
from src.schemas.characteristics.base import BaseCharacteristic


class TransactionType(BaseCharacteristic):
    pass


class TransactionTypeResponse(TransactionType, BaseResponseSchema):
    pass


class TransactionTypeCreate(TransactionType):
    pass


class TransactionTypeUpdate(TransactionType):
    pass
