from src.schemas import BaseResponseSchema

from src.schemas.entities.base import BaseEntity


class Photo(BaseEntity):
    photo_path: str
    photo_thumb: str


class PhotoResponse(Photo, BaseResponseSchema):
    pass


class PhotoCreate(Photo):
    pass


class PhotoUpdate(Photo):
    pass
