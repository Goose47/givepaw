from fastapi import Request
from sqlalchemy import String
from sqlalchemy.orm import mapped_column, Mapped

from src.database.models.base import AbstractModel


class AbstractCharacteristicModel(AbstractModel):
    __abstract__ = True

    title: Mapped[str] = mapped_column(String(256), unique=True, nullable=False, index=True)

    async def __admin_repr__(self, request: Request):
        return f"{self.title}"
