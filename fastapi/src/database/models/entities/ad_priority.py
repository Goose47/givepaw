import datetime
from fastapi import Request

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.database.models.entities.base import AbstractBaseEntityModel


class AdPriority(AbstractBaseEntityModel):
    __tablename__ = "ad_priority"

    priority_id: Mapped[int] = mapped_column(ForeignKey("priority.id"), nullable=False)
    priority: Mapped["Priority"] = relationship(back_populates="ad_priorities", uselist=False, lazy="selectin")

    advertisement_id: Mapped[int] = mapped_column(ForeignKey("advertisement.id"), nullable=False)
    advertisement: Mapped["Advertisement"] = relationship(back_populates="ad_priorities", uselist=False, lazy="selectin")

    start_time: Mapped[datetime.datetime] = mapped_column(nullable=False)
    end_time: Mapped[datetime.datetime] = mapped_column(nullable=False)

    def __repr__(self) -> str:
        return (
            f"AdPriority(id={self.id}, priority_id={self.priority_id}, "
            f"advertisement_id={self.advertisement_id}, start_time={self.start_time}, end_time={self.end_time})")

    async def __admin_repr__(self, request: Request):
        return f"{self.last_name} {self.first_name}, {self.email}"

    async def __admin_select2_repr__(self, request: Request) -> str:
        return f'<div><span>{self.last_name} {self.first_name}, <i>{self.email}</i></span></div>'
