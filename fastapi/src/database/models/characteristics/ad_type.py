from typing import List

from sqlalchemy.orm import Mapped, relationship

from src.database.models.characteristics.base import AbstractCharacteristicModel


class AdType(AbstractCharacteristicModel):
    TYPE_1 = 1
    TYPE_2 = 2
    TYPE_3 = 3

    __tablename__ = "ad_type"

    def __repr__(self) -> str:
        return f"AdType(id={self.id}, title={self.title})"
