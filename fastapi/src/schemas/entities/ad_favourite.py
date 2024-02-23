from src.schemas import BaseResponseSchema
from src.schemas.entities.base import BaseEntity


class AdFavourite(BaseEntity):
    advertisement_id: int
    user_id: int


class AdFavouriteResponse(AdFavourite, BaseResponseSchema):
    pass


class AdFavouriteCreate(AdFavourite):
    pass


class AdFavouriteUpdate(AdFavourite):
    pass
