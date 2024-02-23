from src.schemas import BaseResponseSchema
from src.schemas.entities.base import BaseEntity


class Avatar(BaseEntity):
    photo_path: str
    photo_thumb: str


class AvatarResponse(Avatar, BaseResponseSchema):
    pass


class AvatarCreate(Avatar):
    pass


class AvatarUpdate(Avatar):
    pass
