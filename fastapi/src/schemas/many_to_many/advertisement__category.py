from src.schemas.base import BaseSchema


class AdvertisementCategory(BaseSchema):
    advertisement_id: int
    category_id: int


class AdvertisementCategoryCreate(AdvertisementCategory):
    pass