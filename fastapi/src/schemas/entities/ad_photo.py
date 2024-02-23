
from src.schemas import BaseResponseSchema
from src.schemas.entities.base import BaseEntity


class AdPhoto(BaseEntity):
    photo_id: int
    advertisement_id: int
    is_main: bool

class AdPhotoResponse(AdPhoto, BaseResponseSchema):
    pass


class AdPhotoCreate(AdPhoto):
    pass


class AdPhotoUpdate(AdPhoto):
    pass
