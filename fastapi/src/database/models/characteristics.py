from sqlalchemy import Boolean, Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from base import Base


class PetType(Base):
    __tablename__ = "pet_types"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True, nullable=False)
    title: Mapped[str] = mapped_column(String, unique=True, index=True, nullable=False)


class BloodComponent(Base):
    __tablename__ = "blood_components"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True, nullable=False)
    title: Mapped[str] = mapped_column(String, unique=True, index=True, nullable=False)

    icon: Mapped[str] = mapped_column(String, unique=True, index=True, nullable=True)


class UserRole(Base):
    __tablename__ = "user_roles"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True, nullable=False)
    title: Mapped[str] = mapped_column(String, unique=True, index=True, nullable=False)


class Vaccination(Base):
    __tablename__ = "vaccinations"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True, nullable=False)
    title: Mapped[str] = mapped_column(String, unique=True, index=True, nullable=False)


class ReasonSearch(Base):
    __tablename__ = "reasons_search"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True, nullable=False)
    title: Mapped[str] = mapped_column(String, unique=True, index=True, nullable=False)


class Rhesus(Base):
    __tablename__ = "rhesus"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True, nullable=False)
    title: Mapped[str] = mapped_column(String, unique=True, index=True, nullable=False)


class Region(Base):
    __tablename__ = "regions"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True, nullable=False)
    title: Mapped[str] = mapped_column(String, unique=True, index=True, nullable=False)


class Avatar(Base):
    __tablename__ = "avatars"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True, nullable=False)

    photo_path: Mapped[str] = mapped_column(String, index=True, nullable=True)
    photo_thumb: Mapped[str] = mapped_column(String, index=True, nullable=True)


# TODO: Проверить что нет лишнего unique
