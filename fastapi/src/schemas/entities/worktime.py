import datetime
from src.schemas import BaseResponseSchema

from src.schemas.entities.base import BaseEntity


class Worktime(BaseEntity):
    weekday_id: int
    advertisement_id: int

    start_time: datetime.time
    end_time: datetime.time


class WorktimeResponse(Worktime, BaseResponseSchema):
    pass


class WorktimeCreate(Worktime):
    pass


class WorktimeUpdate(Worktime):
    pass
