from src.schemas import BaseResponseSchema

from src.schemas.entities.base import BaseEntity


class Category(BaseEntity):
    title: str
    order: int

    meta_title: str
    meta_description: str
    url: str

    parent_id: int

    bookable: bool
    map_addressable: bool


class CategoryResponse(Category, BaseResponseSchema):
    pass


class CategoryShort(BaseEntity, BaseResponseSchema):
    title: str


class CategoryCreate(Category):
    pass


class CategoryUpdate(Category):
    pass
