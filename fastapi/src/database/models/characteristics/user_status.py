from typing import ClassVar, List
from fastapi import Request
from sqlalchemy.orm import mapped_column, Mapped, relationship

from src.database.models.characteristics.base import AbstractCharacteristicModel


class UserStatus(AbstractCharacteristicModel):
    ACTIVE = 1
    BLOCKED = 2

    __tablename__ = "user_status"

    is_available: Mapped[bool] = mapped_column(default=True, nullable=False)

    def __repr__(self) -> str:
        return f"UserStatus(id={self.id}, title={self.title}, is_available={self.is_available})"

    async def __admin_repr__(self, request: Request):
        return f"{self.title}"

    async def __admin_select2_repr__(self, request: Request) -> str:
        return f'<div><span>{self.title}</span></div>'
