from src.schemas import BaseResponseSchema
from src.schemas.entities.base import BaseEntity


class AdTag(BaseEntity):
    title: str


class AdTagResponse(AdTag, BaseResponseSchema):
    pass
