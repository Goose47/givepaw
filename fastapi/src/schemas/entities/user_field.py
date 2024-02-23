from src.schemas import BaseResponseSchema

from src.schemas.entities.base import BaseEntity


class UserField(BaseEntity):
    type: str
    title: str

    order: int


class UserFieldResponse(UserField, BaseResponseSchema):
    pass


class UserFieldCreate(UserField):
    pass


class UserFieldUpdate(UserField):
    pass
