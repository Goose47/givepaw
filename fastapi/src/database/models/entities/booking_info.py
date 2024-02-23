from fastapi import Request

from sqlalchemy.orm import mapped_column, Mapped

from src.database.models.entities.base import AbstractBaseEntityModel



class BookingInfo(AbstractBaseEntityModel):
    __tablename__ = "booking_info"

    field: Mapped[str] = mapped_column(nullable=False)

    def __repr__(self) -> str:
        return f"BookingInfo(id={self.id}, field={self.field})"

    async def __admin_repr__(self, request: Request):
        return f"{self.last_name} {self.first_name}, {self.email}"

    async def __admin_select2_repr__(self, request: Request) -> str:
        return f'<div><span>{self.last_name} {self.first_name}, <i>{self.email}</i></span></div>'
