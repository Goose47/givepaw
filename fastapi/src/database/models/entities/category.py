from typing import Optional, List
from fastapi import Request
from sqlalchemy import ForeignKey
from sqlalchemy.orm import mapped_column, Mapped, relationship

from src.database.models.entities.base import AbstractBaseEntityModel


#TODO: ADD TO ADMIN
class Category(AbstractBaseEntityModel):
    __tablename__ = "category"

    title: Mapped[str] = mapped_column(nullable=False)
    order: Mapped[int] = mapped_column(nullable=False)

    meta_title: Mapped[str] = mapped_column(nullable=False)
    meta_description: Mapped[str] = mapped_column(nullable=False)
    url: Mapped[str] = mapped_column(nullable=False)

    parent_id: Mapped[Optional[int]] = mapped_column(ForeignKey("category.id"))
    parent: Mapped["Category"] = relationship()

    bookable: Mapped[bool] = mapped_column(nullable=False, default=False)
    map_addressable: Mapped[bool] = mapped_column(nullable=False, default=False)

    advertisements: Mapped[List["Advertisement"]] = relationship(back_populates="categories",
                                                                 uselist=True, lazy="selectin",
                                                                 secondary="advertisement__category")
    filters: Mapped[List["Filter"]] = relationship(back_populates="categories",
                                                   uselist=True, lazy="selectin", secondary="category__filter")

    def __repr__(self) -> str:
        return (f"Category(id={self.id}, title={self.title}, order={self.order}, meta_title={self.meta_title},"
                f"meta_description={self.meta_description}, url={self.url}, parent_id={self.parent_id},"
                f"bookable={self.bookable}, map_addressable={self.map_addressable})")

    async def __admin_repr__(self, request: Request):
        return f"{self.title}"

    async def __admin_select2_repr__(self, request: Request) -> str:
        return f'<div><span<i>{self.title}</i></span></div>'
