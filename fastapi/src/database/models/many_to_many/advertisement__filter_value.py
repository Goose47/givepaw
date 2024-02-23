from typing import ClassVar

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from src.database.models.base import Base


class AdvertisementFilterValue(Base):
    __tablename__ = "advertisement__filter_value"

    advertisement_id: Mapped[int] = mapped_column(ForeignKey("advertisement.id"), nullable=False, primary_key=True)
    # filter_id
    # filter_content
    # todo: move to entities





    filter_value_id: Mapped[int] = mapped_column(ForeignKey("filter_value.id"), nullable=False, primary_key=True)
