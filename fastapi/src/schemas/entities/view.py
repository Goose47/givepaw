import datetime

from src.schemas import BaseResponseSchema
from src.schemas.entities.base import BaseEntity


class View(BaseEntity):
    advertisement_id: int
    view_count: int
    date: datetime.date


class ViewResponse(View, BaseResponseSchema):
    pass


class ViewCreate(View):
    pass


class ViewUpdate(View):
    pass
