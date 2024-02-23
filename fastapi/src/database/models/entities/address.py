from typing import  Optional
from fastapi import Request

from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.database.models.entities.base import AbstractBaseEntityModel


class Address(AbstractBaseEntityModel):
    __tablename__ = "address"

    address: Mapped[str] = mapped_column(String(256), nullable=False)

    country_id: Mapped[Optional[int]] = mapped_column(ForeignKey("country.id"))
    country: Mapped[Optional["Country"]] = relationship(back_populates="addresses", uselist=False, lazy="selectin")

    city_id: Mapped[Optional[int]] = mapped_column(ForeignKey("city.id"))
    city: Mapped[Optional["City"]] = relationship(back_populates="addresses", uselist=False, lazy="selectin")

    street: Mapped[Optional[str]] = mapped_column(String(64))
    house: Mapped[Optional[str]] = mapped_column(String(32))
    flat: Mapped[Optional[str]] = mapped_column(String(16))

    longitude: Mapped[Optional[float]] = mapped_column()
    latitude: Mapped[Optional[float]] = mapped_column()

    advertisement: Mapped["Advertisement"] = relationship(back_populates="address", uselist=False, lazy="selectin")

    def __repr__(self) -> str:
        return (f"Address(id={self.id}, address={self.address}, country_id={self.country},"
                f"city_id={self.city_id}, street={self.street}, house={self.house}, flat={self.flat},"
                f"longitude={self.longitude}, latitude={self.latitude})")

    async def __admin_repr__(self, request: Request):
        return f"{self.last_name} {self.first_name}, {self.email}"

    async def __admin_select2_repr__(self, request: Request) -> str:
        return f'<div><span>{self.last_name} {self.first_name}, <i>{self.email}</i></span></div>'
