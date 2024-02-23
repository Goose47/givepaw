from typing import Optional

from src.schemas.base import BaseResponseSchema
from src.schemas.characteristics.base import BaseCharacteristic


# checkbox (multiple_select)
# text
# radio (color, select)
# numerical_interval
# date_interval

# в скобках title, отдельная строка -- functional_title

class FilterType(BaseCharacteristic):
    functional_title: str

    interval_placeholder_from: Optional[str]
    interval_placeholder_to: Optional[str]


class FilterTypeResponse(FilterType, BaseResponseSchema):
    pass


class FilterTypeCreate(FilterType):
    pass


class FilterTypeUpdate(FilterType):
    pass
