from src.schemas import BaseResponseSchema

from src.schemas.entities.base import BaseEntity


class Filter(BaseEntity):
    title: str
    filter_type_id: int
    order: int


class FilterResponse(Filter, BaseResponseSchema):
    pass


class FilterCreate(Filter):
    pass


class FilterUpdate(Filter):
    pass
