import datetime

from src.schemas import BaseResponseSchema
from src.schemas.entities.base import BaseEntity


class AdPriority(BaseEntity):
    priority_id: int
    advertisement_id: int

    start_time: datetime.datetime
    end_time: datetime.datetime


class AdPriorityResponse(AdPriority, BaseResponseSchema):
    pass


class AdPriorityCreate(AdPriority):
    pass


class AdPriorityUpdate(AdPriority):
    pass
