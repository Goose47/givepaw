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


class City(Base):
    __tablename__ = "cities"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True, nullable=False)
    title: Mapped[str] = mapped_column(String, unique=True, index=True, nullable=False)

    region_id: Mapped[int] = mapped_column(ForeignKey("regions.id"), nullable=False)


class Pet(Base):
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True, nullable=False)
    pet_blood_group_id: Mapped[int] = mapped_column(ForeignKey("pet_blood_groups.id"), nullable=False)
    breed_id: Mapped[int] = mapped_column(ForeignKey("breeds.id"), nullable=False)

    avatar_id: Mapped[int] = mapped_column(ForeignKey("avatars.id"), nullable=False)
    name: Mapped[str] = mapped_column(String, nullable=False)
    age: Mapped[int] = mapped_column(Integer, nullable=False)


class PetBloodGroup(Base):
    __tablename__ = "pet_blood_groups"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True, nullable=False)
    blood_group: Mapped[str] = mapped_column(String, index=True, nullable=False)

    pet_type_id: Mapped[int] = mapped_column(ForeignKey("pet_types.id"), nullable=False)
    rhesus_id: Mapped[int] = mapped_column(ForeignKey("rhesus.id"), nullable=False)


class UsersConfig(Base):
    __tablename__ = "users_configs"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True, nullable=False)
    phone_number_status: Mapped[int] = mapped_column(Integer, index=True, nullable=False)
    social_networks_status: Mapped[int] = mapped_column(Integer, index=True, nullable=False)
    email_status: Mapped[int] = mapped_column(Integer, index=True, nullable=False)

    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"), nullable=False)


class Breed(Base):
    __tablename__ = "breeds"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True, nullable=False)
    title: Mapped[str] = mapped_column(String, unique=True, index=True, nullable=False)

    pet_type_id: Mapped[int] = mapped_column(ForeignKey("pet_types.id"), nullable=False)


class PetVaccination(Base):
    __table__ = "pet_vaccination"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True, nullable=False)

    pet_type_id: Mapped[int] = mapped_column(ForeignKey("pet_types.id"), nullable=False)
    vaccination_id: Mapped[int] = mapped_column(ForeignKey("vaccinations.id"), nullable=False)
    