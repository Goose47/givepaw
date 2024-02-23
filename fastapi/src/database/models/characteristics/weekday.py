from typing import ClassVar, Optional, List

from sqlalchemy import String
from sqlalchemy.orm import mapped_column, Mapped, relationship

from src.database.models.characteristics.base import AbstractCharacteristicModel


class Weekday(AbstractCharacteristicModel):
    MONDAY = 1
    TUESDAY = 2
    WEDNESDAY = 3
    THURSDAY = 4
    FRIDAY = 5
    SATURDAY = 6
    SUNDAY = 7
    __tablename__ = "weekday"

    short_title: Mapped[Optional[str]] = mapped_column(String(8), unique=True)
    order: Mapped[int] = mapped_column()

    worktimes: Mapped[List["Worktime"]] = relationship(back_populates="weekday", uselist=True, lazy="selectin")

    def __repr__(self) -> str:
        return f"Weekday(id={self.id}, title={self.title}, short_title={self.short_title}, order={self.order})"
