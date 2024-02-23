from fastapi import Request

from sqlalchemy import ForeignKey
from sqlalchemy.orm import mapped_column, Mapped, relationship

from src.database.models.entities.base import AbstractBaseEntityModelTime


class Review(AbstractBaseEntityModelTime):
    __tablename__ = "review"

    advertisement_id: Mapped[int] = mapped_column(ForeignKey("advertisement.id"), nullable=False)
    advertisement: Mapped["Advertisement"] = relationship(back_populates="reviews", uselist=False, lazy="selectin")

    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"), nullable=False)
    user: Mapped["User"] = relationship(back_populates="reviews", uselist=False, lazy="selectin")

    text: Mapped[str] = mapped_column(nullable=False)
    rating: Mapped[int] = mapped_column(nullable=False)

    def __repr__(self) -> str:
        return (f"Review(id={self.id}, advertisement_id={self.advertisement_id}, user_id={self.user_id},"
                f"text={self.text}, rating={self.rating})")

    async def __admin_repr__(self, request: Request):
        return f"{self.last_name} {self.first_name}, {self.email}"

    async def __admin_select2_repr__(self, request: Request) -> str:
        return f'<div><span>{self.last_name} {self.first_name}, <i>{self.email}</i></span></div>'
