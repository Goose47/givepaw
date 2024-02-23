from typing import Optional, List
from fastapi import Request
from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import mapped_column, Mapped, relationship

from src.database.models.entities.base import AbstractBaseEntityModel

#TODO: ADD TO ADMIN
class FilterValue(AbstractBaseEntityModel):
    __tablename__ = "filter_value"

    filter_id: Mapped[int] = mapped_column(ForeignKey("filter.id"), nullable=False)
    filter: Mapped["Filter"] = relationship(back_populates="filter_values", uselist=False, lazy="selectin")

    value: Mapped[str] = mapped_column(String(256), nullable=False)
    hint_html: Mapped[Optional[str]] = mapped_column(String(256))
    order: Mapped[int] = mapped_column(nullable=False)

    advertisements: Mapped[List["Advertisement"]] = relationship(back_populates="filter_values",
                                                                 uselist=True, lazy="selectin",
                                                                 secondary="advertisement__filter_value")

    def __repr__(self) -> str:
        return (f"FilterValue(id={self.id}, value={self.value}, filter_id={self.filter_id},"
                f" order={self.order}, hint_html={self.hint_html})")

    async def __admin_repr__(self, request: Request):
        return f"{self.last_name} {self.first_name}, {self.email}"

    async def __admin_select2_repr__(self, request: Request) -> str:
        return f'<div><span>{self.last_name} {self.first_name}, <i>{self.email}</i></span></div>'
