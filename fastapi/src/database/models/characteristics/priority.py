from typing import ClassVar, List

from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.database.models.characteristics.base import AbstractCharacteristicModel


class Priority(AbstractCharacteristicModel):
    __tablename__ = "priority"

    priority: Mapped[int] = mapped_column()

    ad_priorities: Mapped[List["AdPriority"]] = relationship(back_populates="priority", uselist=True, lazy="selectin")

    def __repr__(self) -> str:
        return f"Priority(id={self.id}, title={self.title})"
