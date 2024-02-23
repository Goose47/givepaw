import datetime
from typing import Optional
from fastapi import Request
from sqlalchemy.orm import mapped_column, Mapped

from src.database.models.base import AbstractModel


class AbstractBaseEntityModel(AbstractModel):
    __abstract__ = True


class AbstractBaseEntityModelTime(AbstractBaseEntityModel):
    __abstract__ = True

    created_at: Mapped[datetime.datetime] = mapped_column(nullable=False, default=datetime.datetime.now())
    updated_at: Mapped[datetime.datetime] = mapped_column(nullable=False, default=datetime.datetime.now())
    deleted_at: Mapped[Optional[datetime.datetime]] = mapped_column(nullable=True)
