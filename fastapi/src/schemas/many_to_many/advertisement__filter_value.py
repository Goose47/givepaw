from src.schemas.base import BaseSchema


class AdvertisementFilterValue(BaseSchema):
    advertisement_id: int
    filter_value_id: int


class AdvertisementCategoryCreate(AdvertisementFilterValue):
    pass
