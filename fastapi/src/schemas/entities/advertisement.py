from typing import Optional, List, Dict, Union, Any

from fastapi.exceptions import RequestValidationError
from pydantic import field_validator, validator, BaseConfig, ConfigDict, root_validator, model_validator, Field

from src.schemas import BaseResponseSchema, Category, Filter, FilterValue, Address, AddressCreate
from src.schemas.entities.base import BaseEntity


class Advertisement(BaseEntity):
    title: str
    user_description: str
    address_id: Optional[int]

    user_id: int

    ad_status_id: int
    ad_type_id: int  # booking, sell

    price: Optional[float]


class AdvertisementResponse(Advertisement, BaseResponseSchema):
    pass


class AdvertisementCreate(Advertisement):
    pass


class AdvertisementPost(BaseEntity):
    title: str = Field(None, validate_default=True)  # for validation
    user_description:str =  Field(None, validate_default=True)
    categories: Optional[List[int]] = Field(None, validate_default=True)  # essential?
    filters: Dict[int, Union[str, int]] = Field(None, validate_default=True)  # Filter, FilterValue
    ad_type_id: int = Field(None, validate_default=True)
    address: Optional[AddressCreate] = Field(None, validate_default=True)
    address_id: Optional[int] = Field(None, validate_default=True)
    price: float = Field(None, validate_default=True)


    """
    @model_validator(mode="before")
    def validate_advertisement(self):
        errors = []

        if 'title' not in self:
            errors.append({"advertisement.title": "Необходимо ввести заголовок объявления."})

        if 'user_description' not in self:
            errors.append({"advertisement.user_description": "Необходимо ввести описание объявления."})

        if 'categories' not in self:
            errors.append({"advertisement.user_description": "UserDescription is not specified"})

        if errors:
            raise RequestValidationError(errors=errors)
        return self

    @field_validator("*", mode="before")
    def not_none(cls, v, field):
        if all(
                (
                        # Cater for the occasion where field.default in (0, False)
                        getattr(field, "default", None) is not None,
                        v is None,
                )
        ):
            return field.default
        else:
            return v
    """


class AdvertisementUpdate(Advertisement):
    pass
