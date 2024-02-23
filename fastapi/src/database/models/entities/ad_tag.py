from typing import List
from fastapi import Request
from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.database.models.entities.base import AbstractBaseEntityModel


# TODO: ADD TO ADMIN
class AdTag(AbstractBaseEntityModel):
    __tablename__ = "ad_tag"

    title: Mapped[str] = mapped_column(String(256), nullable=False, unique=True)

    advertisements: Mapped[List["Advertisement"]] = relationship(back_populates="ad_tags",
                                                                 uselist=True, lazy="selectin",
                                                                 secondary="advertisement__ad_tag")

    def __repr__(self) -> str:
        return f"AdTag(id={self.id}, title={self.title})"

    async def __admin_repr__(self, request: Request):
        return f"{self.last_name} {self.first_name}, {self.email}"

    async def __admin_select2_repr__(self, request: Request) -> str:
        return f'<div><span>{self.last_name} {self.first_name}, <i>{self.email}</i></span></div>'
