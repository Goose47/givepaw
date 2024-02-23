from typing import ClassVar

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from src.database.models.base import Base


class AdvertisementCategory(Base):
    __tablename__ = "advertisement__category"

    advertisement_id: Mapped[int] = mapped_column(ForeignKey("advertisement.id"), nullable=False, primary_key=True)
    category_id: Mapped[int] = mapped_column(ForeignKey("category.id"), nullable=False, primary_key=True)
