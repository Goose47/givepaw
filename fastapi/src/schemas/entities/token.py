from src.schemas.entities.base import BaseEntity


class Token(BaseEntity):
    access_token: str
    token_type: str
