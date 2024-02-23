from typing import Optional
from src.schemas import BaseResponseSchema

from src.schemas.entities.base import BaseEntity


class FilterValue(BaseEntity):
    filter_id: int
    value: str
    hint_html: Optional[str]
    order: int


class FilterValueResponse(FilterValue, BaseResponseSchema):
    pass


class FilterValueCreate(FilterValue):
    pass


class FilterValueUpdate(FilterValue):
    pass
