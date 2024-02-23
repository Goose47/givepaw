from typing import ClassVar

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from src.database.models.base import Base


class CategoryFilter(Base):
    __tablename__ = "category__filter"

    filter_id: Mapped[int] = mapped_column(ForeignKey("filter.id"), nullable=False, primary_key=True)
    category_id: Mapped[int] = mapped_column(ForeignKey("category.id"), nullable=False, primary_key=True)
