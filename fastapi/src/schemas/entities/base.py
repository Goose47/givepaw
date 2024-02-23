import datetime
from typing import Optional

from src.schemas.base import BaseSchema


class BaseEntity(BaseSchema):
    pass


class BaseEntityTime(BaseEntity):
    created_at: Optional[datetime.datetime] = None
    updated_at: Optional[datetime.datetime] = None
    deleted_at: Optional[datetime.datetime] = None
