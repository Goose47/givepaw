from src.schemas.base import BaseResponseSchema
from src.schemas.characteristics.base import BaseCharacteristic


class City(BaseCharacteristic):
    pass


class CityResponse(City, BaseResponseSchema):
    pass


class CityCreate(City):
    pass


class CityUpdate(City):
    pass
