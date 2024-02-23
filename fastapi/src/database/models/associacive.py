from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import Mapped, mapped_column
from base import Base


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True, nullable=False)

    surname: Mapped[str] = mapped_column(String, nullable=False)
    name: Mapped[str] = mapped_column(String, nullable=False)
    patronymic: Mapped[str] = mapped_column(String)

    username: Mapped[str] = mapped_column(String, unique=True, index=True, nullable=False)

    email: Mapped[str] = mapped_column(String, unique=True, index=True, nullable=False)

    password: Mapped[str] = mapped_column(String, nullable=False)
    user_role_id: Mapped[int] = mapped_column(ForeignKey("user_roles.id"), nullable=False)

    # google
    # vk
    # tg

    city_id: Mapped[int] = mapped_column(ForeignKey("cities.id"), nullable=False)

    avatar_id: Mapped[int] = mapped_column(ForeignKey("avatars.id"), nullable=False)


class Pet(Base):
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True, nullable=False)
    pet_blood_group_id: Mapped[int] = mapped_column(ForeignKey("pet_blood_groups.id"), nullable=False)
    breed_id: Mapped[int] = mapped_column(ForeignKey("breeds.id"), nullable=False)

    avatar_id: Mapped[int] = mapped_column(ForeignKey("avatars.id"), nullable=False)
    name: Mapped[str] = mapped_column(String, nullable=False)
    age: Mapped[int] = mapped_column(Integer, nullable=False)
