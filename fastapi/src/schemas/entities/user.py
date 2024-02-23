from typing import Optional
import datetime

from pydantic import EmailStr, BaseModel
from pydantic_extra_types.phone_numbers import PhoneNumber

from src.database import models
from src.schemas.entities.base import BaseEntityTime, BaseEntity
from src.schemas import BaseResponseSchema, Avatar


class User(BaseEntityTime):
    first_name: str
    last_name: str

    email: EmailStr

    user_status_id: int
    phone_number: PhoneNumber

    avatar_id: int  # photo_id

    # GOOGLE, FACEBOOK...

    phone_verified_at: Optional[datetime.datetime]
    email_verified_at: Optional[datetime.datetime]


class UserResponse(BaseResponseSchema):
    pass


class UserShort(BaseEntity, BaseResponseSchema):
    first_name: str
    last_name: str
    avatar: Optional[Avatar]  # todo: remove optional


class UserCreate(User):
    pass


class UserUpdate(User):
    pass


def create_user_short(user: models.User):
    user = UserShort(
        id=user.id,
        first_name=user.first_name,
        last_name=user.last_name,
        avatar=user.avatar,
    )
    return user
