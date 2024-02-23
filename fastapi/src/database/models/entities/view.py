import datetime
from fastapi import Request

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.database.models.entities.base import AbstractBaseEntityModel



class View(AbstractBaseEntityModel):
    __tablename__ = "view"

    advertisement_id: Mapped[int] = mapped_column(ForeignKey("advertisement.id"), nullable=False)
    advertisement: Mapped["Advertisement"] = relationship(back_populates="views", uselist=False, lazy="selectin")

    view_count: Mapped[int] = mapped_column(nullable=False)

    date: Mapped[datetime.date] = mapped_column(nullable=False)

    def __repr__(self) -> str:
        return (
            f"View(id={self.id}, advertisement_id={self.advertisement_id}, view_count={self.view_count}, date={self.date})")

    async def __admin_repr__(self, request: Request):
        return f"{self.last_name} {self.first_name}, {self.email}"

    async def __admin_select2_repr__(self, request: Request) -> str:
        return f'<div><span>{self.last_name} {self.first_name}, <i>{self.email}</i></span></div>'
