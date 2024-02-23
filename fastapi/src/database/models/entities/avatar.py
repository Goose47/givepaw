from fastapi import Request

from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.database.models.entities.base import AbstractBaseEntityModel


class Avatar(AbstractBaseEntityModel):
    __tablename__ = "avatar"

    photo_path: Mapped[str] = mapped_column(String, nullable=False)
    photo_thumb: Mapped[str] = mapped_column(String)

    user: Mapped["User"] = relationship(back_populates="avatar", uselist=False, lazy="selectin")

    def __repr__(self) -> str:
        return f"Avatar(id={self.id}, photo_path={self.photo_path})"

    async def __admin_repr__(self, request: Request):
        return f"{self.last_name} {self.first_name}, {self.email}"

    async def __admin_select2_repr__(self, request: Request) -> str:
        return f'<div><span>{self.last_name} {self.first_name}, <i>{self.email}</i></span></div>'
