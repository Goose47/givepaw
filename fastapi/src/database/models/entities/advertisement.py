from typing import Optional, List
from fastapi import Request

from sqlalchemy import String, Text, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.database.models.entities.base import AbstractBaseEntityModelTime


#TODO: ADD TO ADMIN, VIEW
class Advertisement(AbstractBaseEntityModelTime):
    __tablename__ = "advertisement"

    title: Mapped[str] = mapped_column(String(128), nullable=False)
    user_description: Mapped[str] = mapped_column(Text, nullable=False)

    address_id: Mapped[Optional[int]] = mapped_column(ForeignKey("address.id"))
    address: Mapped["Address"] = relationship(back_populates="advertisement", uselist=False, lazy="selectin")

    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"), nullable=False)
    user: Mapped["User"] = relationship(back_populates="advertisements", uselist=False, lazy="selectin")

    ad_status_id: Mapped[int] = mapped_column(ForeignKey("ad_status.id"),
                                              nullable=False)
    ad_status: Mapped["AdStatus"] = relationship(uselist=False, lazy="selectin")

    ad_type_id: Mapped[int] = mapped_column(ForeignKey("ad_type.id"),
                                            nullable=False)  # booking, sell
    ad_type: Mapped["AdType"] = relationship(uselist=False, lazy="selectin")

    price: Mapped[Optional[float]] = mapped_column(nullable=False)

    ad_bookings_available: Mapped[List["AdBookingAvailable"]] = relationship(back_populates="advertisement",
                                                                             uselist=True, lazy="selectin")
    ad_favourites: Mapped[List["AdFavourite"]] = relationship(back_populates="advertisement",
                                                              uselist=True, lazy="selectin")

    ad_photos: Mapped[List["AdPhoto"]] = relationship(back_populates="advertisement", uselist=True, lazy="selectin")

    ad_priorities: Mapped[List["AdPriority"]] = relationship(back_populates="advertisement", uselist=True,
                                                             lazy="selectin")

    ad_tags: Mapped[List["AdTag"]] = relationship(back_populates="advertisements",
                                                  uselist=True, lazy="selectin", secondary="advertisement__ad_tag")
    bookings: Mapped[List["Booking"]] = relationship(back_populates="advertisement", uselist=True, lazy="selectin")

    categories: Mapped[List["Category"]] = relationship(back_populates="advertisements",
                                                        uselist=True, lazy="selectin",
                                                        secondary="advertisement__category")
    reviews: Mapped[List["Review"]] = relationship(back_populates="advertisement", uselist=True, lazy="selectin")

    views: Mapped[List["View"]] = relationship(back_populates="advertisement", uselist=True, lazy="selectin")

    worktimes: Mapped[List["Worktime"]] = relationship(back_populates="advertisement", uselist=True, lazy="selectin")

    filter_values: Mapped[List["FilterValue"]] = relationship(back_populates="advertisements",
                                                              uselist=True, lazy="selectin",
                                                              secondary="advertisement__filter_value")
    transactions: Mapped[List["Transaction"]] = relationship(back_populates="advertisement", uselist=True,
                                                             lazy="selectin")

    def __repr__(self) -> str:
        return (f"Advertisement(id={self.id}, title={self.title}, user_description={self.user_description},"
                f"address_id={self.address_id}, user_id={self.user_id}, ad_status_id={self.ad_status_id},"
                f"ad_type_id={self.ad_type_id}, price={self.price})")

    async def __admin_repr__(self, request: Request):
        return f"{self.id}|{self.title}|{self.user}"

    async def __admin_select2_repr__(self, request: Request) -> str:
        return f'<div><span>{self.last_name} {self.first_name}, <i>{self.email}</i></span></div>'
