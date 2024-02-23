from typing import List

from sqlalchemy.orm import Mapped, relationship

from src.database.models.characteristics.base import AbstractCharacteristicModel


class UserRole(AbstractCharacteristicModel):
    ADMIN = 1
    SELLER = 2
    CONSUMER = 3

    __tablename__ = "user_role"

    # TODO: Найти, где использовали. Дописать relationship
    # users: Mapped[List["User"]] = relationship(back_populates="user_role", uselist=True, lazy="selectin")

    def __repr__(self) -> str:
        return f"UserRole(id={self.id}, title={self.title})"
