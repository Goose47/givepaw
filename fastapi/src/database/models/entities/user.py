from typing import Optional, List
import datetime
from sqlalchemy_utils import EmailType, PhoneNumberType
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from fastapi import Request
from src.database.models.entities.base import AbstractBaseEntityModelTime


#TODO: ADD TO ADMIN
class User(AbstractBaseEntityModelTime):
    __tablename__ = "users"

    first_name: Mapped[str] = mapped_column(nullable=False)
    last_name: Mapped[str] = mapped_column(nullable=False)

    email: Mapped[str] = mapped_column(EmailType, nullable=False, unique=True)

    user_status_id: Mapped[int] = mapped_column(ForeignKey("user_status.id"), nullable=False)
    user_status: Mapped["UserStatus"] = relationship(uselist=False, lazy="selectin")

    phone_number: Mapped[str] = mapped_column(PhoneNumberType)  # TODO: nullable= False?, unique = True?

    avatar_id: Mapped[Optional[int]] = mapped_column(ForeignKey("avatar.id"),
                                                     nullable=True)  # TODO: default avatar? Optional?
    avatar: Mapped["Avatar"] = relationship(back_populates="user", uselist=False, lazy="selectin")

    password: Mapped[str] = mapped_column(nullable=True)

    # TODO: GOOGLE, FACEBOOK...

    phone_verified_at: Mapped[Optional[datetime.datetime]] = mapped_column()
    email_verified_at: Mapped[Optional[datetime.datetime]] = mapped_column()

    ad_favourites: Mapped[List["AdFavourite"]] = relationship(back_populates="user",
                                                              uselist=True, lazy="selectin")
    advertisements: Mapped[List["Advertisement"]] = relationship(back_populates="user",
                                                                 uselist=True, lazy="selectin")

    bookings: Mapped[List["Booking"]] = relationship(back_populates="user", uselist=True, lazy="selectin")

    reviews: Mapped[List["Review"]] = relationship(back_populates="user", uselist=True, lazy="selectin")

    notifications: Mapped[List["UserNotification"]] = relationship(back_populates="user", uselist=True, lazy="selectin")

    user_fields: Mapped[List["UserField"]] = relationship(back_populates="users",
                                                          uselist=True, lazy="selectin", secondary="user__user_field")

    def __repr__(self) -> str:
        return (
            f"User(id={self.id}, first_name={self.first_name}, last_name={self.last_name}, email={self.email}, user_status_id={self.user_status_id})")

    async def __admin_repr__(self, request: Request):
        return f"{self.last_name} {self.first_name}, {self.email}"

    async def __admin_select2_repr__(self, request: Request) -> str:
        return f'<div><span>{self.last_name} {self.first_name}, <i>{self.email}</i></span></div>'

    async def __admin_repr__(self, request: Request):
        return f"{self.last_name} {self.first_name}, {self.email}"

    async def __admin_select2_repr__(self, request: Request) -> str:
        return f'<div><span>{self.last_name} {self.first_name}, <i>{self.email}</i></span></div>'
