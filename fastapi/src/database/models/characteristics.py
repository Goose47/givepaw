from sqlalchemy import Integer, String

from sqlalchemy.orm import Mapped, mapped_column
from src.database.models.base import Base
from src.config.app.config import settings_app


class PetType(Base):
    __tablename__ = "pet_types"
    extend_existing = True

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True, nullable=False)
    title: Mapped[str] = mapped_column(String, unique=True, index=True, nullable=False)

    icon: Mapped[str] = mapped_column(String, nullable=True)

    @property
    def link(self):
        return settings_app.APP_URL + '/files/assets/' + self.icon


class BloodComponent(Base):
    __tablename__ = "blood_components"
    extend_existing = True

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True, nullable=False)
    title: Mapped[str] = mapped_column(String, unique=True, index=True, nullable=False)

    icon: Mapped[str] = mapped_column(String, nullable=True)


class UserRole(Base):
    __tablename__ = "user_roles"
    extend_existing = True

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True, nullable=False)
    title: Mapped[str] = mapped_column(String, unique=True, index=True, nullable=False)


class Vaccination(Base):
    __tablename__ = "vaccinations"
    extend_existing = True

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True, nullable=False)
    title: Mapped[str] = mapped_column(String, unique=True, index=True, nullable=False)


class Rhesus(Base):
    __tablename__ = "rhesus"
    extend_existing = True

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True, nullable=False)
    title: Mapped[str] = mapped_column(String, unique=True, index=True, nullable=False)


class Region(Base):
    __tablename__ = "regions"
    extend_existing = True

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True, nullable=False)
    title: Mapped[str] = mapped_column(String, unique=True, index=True, nullable=False)


class Avatar(Base):
    __tablename__ = "avatars"
    extend_existing = True

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True, nullable=False)

    photo_path: Mapped[str] = mapped_column(String, nullable=False)
    photo_thumb: Mapped[str] = mapped_column(String, nullable=True)


class BloodGroup(Base):
    __tablename__ = "blood_groups"
    extend_existing = True

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True, nullable=False)
    title: Mapped[str] = mapped_column(String, unique=True, index=True, nullable=False)
