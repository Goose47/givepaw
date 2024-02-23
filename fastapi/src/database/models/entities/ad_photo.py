from fastapi import Request

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.database.models.entities.base import AbstractBaseEntityModel


class AdPhoto(AbstractBaseEntityModel):
    __tablename__ = "ad_photo"

    photo_id: Mapped[int] = mapped_column(ForeignKey("photo.id"), nullable=False)
    photo: Mapped["Photo"] = relationship(back_populates="ad_photo", uselist=False, lazy="selectin")

    advertisement_id: Mapped[int] = mapped_column(ForeignKey("advertisement.id"), nullable=False)
    advertisement: Mapped["Advertisement"] = relationship(back_populates="ad_photos", uselist=False, lazy="selectin")

    is_main: Mapped[bool] = mapped_column(default=False, nullable=False)

    def __repr__(self) -> str:
        return (
            f"AdPhoto(id={self.id}, photo_id={self.photo_id}, "
            f"advertisement_id={self.advertisement_id}, is_main={self.is_main})")

    async def __admin_repr__(self, request: Request):
        return f"{self.last_name} {self.first_name}, {self.email}"

    async def __admin_select2_repr__(self, request: Request) -> str:
        return f'<div><span>{self.last_name} {self.first_name}, <i>{self.email}</i></span></div>'
