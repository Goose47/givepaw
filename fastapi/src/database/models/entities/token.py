from sqlalchemy.orm import Mapped, mapped_column
from fastapi import Request
from src.database.models.entities.base import AbstractBaseEntityModelTime


class Token(AbstractBaseEntityModelTime):
    __tablename__ = "token"

    access_token: Mapped[str] = mapped_column(nullable=False)
    token_type: Mapped[str] = mapped_column(nullable=False)

    async def __admin_repr__(self, request: Request):
        return f"{self.last_name} {self.first_name}, {self.email}"

    async def __admin_select2_repr__(self, request: Request) -> str:
        return f'<div><span>{self.last_name} {self.first_name}, <i>{self.email}</i></span></div>'
