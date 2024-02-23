from typing import ClassVar

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from src.database.models.base import Base


class UserUserField(Base):
    __tablename__ = "user__user_field"

    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"), nullable=False, primary_key=True)
    user_field_id: Mapped[int] = mapped_column(ForeignKey("user_field.id"), nullable=False, primary_key=True)
    # todo: user_field_value str
    # todo: move to entities