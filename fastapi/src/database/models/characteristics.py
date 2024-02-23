from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
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

    icon: Mapped[str] = mapped_column(String, unique=True, index=True, nullable=False)


class UserRole(Base):
    __tablename__ = "user_roles"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True, nullable=False)
    title: Mapped[str] = mapped_column(String, unique=True, index=True, nullable=False)


class Vaccination(Base):
    __tablename__ = "vaccinations"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True, nullable=False)
    title: Mapped[str] = mapped_column(String, unique=True, index=True, nullable=False)


class City(Base):
    __tablename__ = "cities"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True, nullable=False)
    title: Mapped[str] = mapped_column(String, unique=True, index=True, nullable=False)

    region_id: Mapped[int] = mapped_column(ForeignKey("regions.id"), nullable=False)


class ReasonSearch(Base):
    __tablename__ = "reasons_search"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True, nullable=False)
    title: Mapped[str] = mapped_column(String, unique=True, index=True, nullable=False)


class Rhesus(Base):
    __tablename__ = "rhesus"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True, nullable=False)
    title: Mapped[str] = mapped_column(String, unique=True, index=True, nullable=False)


class Breed(Base):
    __tablename__ = "breeds"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True, nullable=False)
    title: Mapped[str] = mapped_column(String, unique=True, index=True, nullable=False)
    
    
class Region(Base):
    __tablename__ = "regions"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True, nullable=False)
    title: Mapped[str] = mapped_column(String, unique=True, index=True, nullable=False)


class UsersConfig(Base):
    __tablename__ = "users_configs"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True, nullable=False)
    phone_number_status: Mapped[int] = mapped_column(Integer, index=True, nullable=False)
    social_networks_status: Mapped[int] = mapped_column(Integer, index=True, nullable=False)
    email_status: Mapped[int] = mapped_column(Integer, index=True, nullable=False)

    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"), nullable=False)

# TODO: Проверить что нет лишнего unique
# TODO: Перенести модельки в ассоциативные
