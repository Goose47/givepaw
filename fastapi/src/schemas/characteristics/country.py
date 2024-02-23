from src.schemas.base import BaseResponseSchema
from src.schemas.characteristics.base import BaseCharacteristic


class Country(BaseCharacteristic):
    pass


class CountryResponse(Country, BaseResponseSchema):
    pass


class CountryCreate(Country):
    pass


class CountryUpdate(Country):
    pass
