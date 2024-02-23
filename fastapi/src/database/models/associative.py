import datetime

from sqlalchemy import ForeignKey, Integer, String, Float, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship
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
    user_role: Mapped["UserRole"] = relationship(uselist=False, lazy="selectin")
    # google
    # vk
    # tg

    # TODO: СДЕЛАТЬ СОЦ. СЕТИ, НОВАЯ ТАБЛИЦА

    city_id: Mapped[int] = mapped_column(ForeignKey("cities.id"), nullable=False)

    avatar_id: Mapped[int] = mapped_column(ForeignKey("avatars.id"), nullable=False)


class City(Base):
    __tablename__ = "cities"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True, nullable=False)
    title: Mapped[str] = mapped_column(String, unique=True, index=True, nullable=False)

    region_id: Mapped[int] = mapped_column(ForeignKey("regions.id"), nullable=False)
    region: Mapped["Region"] = relationship(uselist=False, lazy="selectin")


class Pet(Base):
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True, nullable=False)
    blood_group_id: Mapped[int] = mapped_column(ForeignKey("pet_blood_groups.id"))
    breed_id: Mapped[int] = mapped_column(ForeignKey("breeds.id"), nullable=False)
    breed: Mapped[str] = mapped_column(String)
    pet_type_id: Mapped[int] = mapped_column(ForeignKey("pet_types.id"))
    avatar_id: Mapped[int] = mapped_column(ForeignKey("avatars.id"), nullable=False)
    name: Mapped[str] = mapped_column(String, nullable=False)
    age: Mapped[int] = mapped_column(Integer, nullable=False)
    weight: Mapped[float] = mapped_column(Float, nullable=False)
    user_id: Mapped[int] = mapped_column(Integer, nullable=False)


class PetBloodGroup(Base):
    __tablename__ = "pet_blood_groups"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True, nullable=False)
    blood_group: Mapped[str] = mapped_column(String, index=True)

    pet_type_id: Mapped[int] = mapped_column(ForeignKey("pet_types.id"), nullable=False)
    rhesus_id: Mapped[int] = mapped_column(ForeignKey("rhesus.id"))


class UsersConfig(Base):
    __tablename__ = "users_configs"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True, nullable=False)
    phone_number_status: Mapped[int] = mapped_column(Integer, index=True, nullable=False)
    social_networks_status: Mapped[int] = mapped_column(Integer, index=True, nullable=False)
    email_status: Mapped[int] = mapped_column(Integer, index=True, nullable=False)

    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"), nullable=False)


class UserNetwork(Base):
    __tablename__ = "user_networks"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True, nullable=False)
    telegram: Mapped[str] = mapped_column(String)
    vk: Mapped[str] = mapped_column(String)


class Breed(Base):
    __tablename__ = "breeds"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True, nullable=False)
    title: Mapped[str] = mapped_column(String, unique=True, index=True, nullable=False)

    pet_type_id: Mapped[int] = mapped_column(ForeignKey("pet_types.id"), nullable=False)


class Demand(Base):
    __tablename__ = "demands"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True, nullable=False)

    reason_search_id: Mapped[int] = mapped_column(ForeignKey("reasons_search.id"), nullable=False)
    information: Mapped[int] = mapped_column(Text)
    blood_component_id: Mapped[int] = mapped_column(ForeignKey("blood_components.id"), nullable=False)

    blood_amount: Mapped[int] = mapped_column(Integer, nullable=False)
    donor_amount: Mapped[int] = mapped_column(Integer, nullable=False)

    pet_id: Mapped[int] = mapped_column(ForeignKey("pets.id"), nullable=False)

    clinic_id: Mapped[int] = mapped_column(ForeignKey("clinics.id"), nullable=False)
    end_actual_date: Mapped[datetime.date] = mapped_column(nullable=False)


class Clinic(Base):
    __tablename__ = "clinics"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True, nullable=False)
    title: Mapped[str] = mapped_column(String, unique=True, index=True, nullable=False)
    address: Mapped[str] = mapped_column(String, unique=True, index=True, nullable=False)
    email: Mapped[str] = mapped_column(String, unique=True, index=True, nullable=False)
    phone: Mapped[str] = mapped_column(String, unique=True, index=True, nullable=False)

    city_id: Mapped[int] = mapped_column(ForeignKey("cities.id"), nullable=False)
