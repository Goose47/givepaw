from typing import List

from sqlalchemy.orm import Mapped, relationship

from src.database.models.characteristics.base import AbstractCharacteristicModel


class City(AbstractCharacteristicModel):
    __tablename__ = "city"

    addresses: Mapped[List["Address"]] = relationship(back_populates="city", uselist=True, lazy="selectin")

    def __repr__(self) -> str:
        return f"City(id={self.id}, title={self.title})"
