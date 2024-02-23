from fastapi import Request

from sqlalchemy import String, ForeignKey, Text
from sqlalchemy.orm import mapped_column, Mapped, relationship

from src.database.models.entities.base import AbstractBaseEntityModelTime


class UserNotification(AbstractBaseEntityModelTime):
    __tablename__ = "user_notification"

    title: Mapped[str] = mapped_column(String(256), nullable=False)
    description: Mapped[str] = mapped_column(Text, nullable=False)

    notification_type: Mapped[str] = mapped_column(Text,
                                                             nullable=False)  # ПОЛИМОРФНЫЙ. "models/entities/category/booking"
    notification_content: Mapped[int] = mapped_column(Text,
                                                                nullable=False)  # ПОЛИМОРФНЫЙ  # TODO: Тюм, разберись, пж

    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"), nullable=False)
    user: Mapped["User"] = relationship(back_populates="notifications", uselist=False, lazy="selectin")

    def __repr__(self) -> str:
        return (
            f"UserNotification(id={self.id}, title={self.title}, description={self.description}, user_id={self.user_id})")

    async def __admin_repr__(self, request: Request):
        return f"{self.last_name} {self.first_name}, {self.email}"

    async def __admin_select2_repr__(self, request: Request) -> str:
        return f'<div><span>{self.last_name} {self.first_name}, <i>{self.email}</i></span></div>'
