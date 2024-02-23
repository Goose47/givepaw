import datetime
from typing import List

from sqlalchemy import ForeignKey, Integer, String, Float, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship
from src.database.models.base import Base


class User(Base):
    __tablename__ = "users"
    extend_existing = True

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

    city_id: Mapped[int] = mapped_column(ForeignKey("cities.id"), nullable=False)
    city: Mapped["City"] = relationship(uselist=False, lazy="selectin")

    avatar_id: Mapped[int] = mapped_column(ForeignKey("avatars.id"), nullable=True)
    avatar: Mapped["Avatar"] = relationship(uselist=False, lazy="selectin")


class City(Base):
    __tablename__ = "cities"
    extend_existing = True

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True, nullable=False)
    title: Mapped[str] = mapped_column(String, unique=True, index=True, nullable=False)

    region_id: Mapped[int] = mapped_column(ForeignKey("regions.id"), nullable=False)
    region: Mapped["Region"] = relationship(uselist=False, lazy="selectin")


class Pet(Base):
    __tablename__ = "pets"
    extend_existing = True

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True, nullable=False)

    blood_group_id: Mapped[int] = mapped_column(ForeignKey("pet_blood_groups.id"))
    blood_group: Mapped["PetBloodGroup"] = relationship(uselist=False, lazy="selectin")

    breed_id: Mapped[int] = mapped_column(ForeignKey("breeds.id"), nullable=False)
    _breed: Mapped["Breed"] = relationship(uselist=False, lazy="selectin")

    breed: Mapped[str] = mapped_column(String)

    pet_type_id: Mapped[int] = mapped_column(ForeignKey("pet_types.id"))
    pet_type: Mapped["PetType"] = relationship(uselist=False, lazy="selectin")

    avatar_id: Mapped[int] = mapped_column(ForeignKey("avatars.id"), nullable=False)
    avatar: Mapped["Avatar"] = relationship(uselist=False, lazy="selectin")

    name: Mapped[str] = mapped_column(String, nullable=False)
    age: Mapped[int] = mapped_column(Integer, nullable=False)
    weight: Mapped[float] = mapped_column(Float, nullable=False)

    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"), nullable=False)
    user: Mapped["User"] = relationship(uselist=False, lazy="selectin")

    vaccinations: Mapped[List["Vaccination"]] = relationship(uselist=True, lazy="selectin",
                                                             secondary="pet__vaccinations")


class PetBloodGroup(Base):
    __tablename__ = "pet_blood_groups"
    extend_existing = True

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True, nullable=False)

    blood_group_id: Mapped[int] = mapped_column(ForeignKey("blood_groups.id"), index=True)
    blood_group: Mapped["BloodGroup"] = relationship(uselist=False, lazy="selectin")

    pet_type_id: Mapped[int] = mapped_column(ForeignKey("pet_types.id"), nullable=False)
    pet_type: Mapped["PetType"] = relationship(uselist=False, lazy="selectin")

    rhesus_id: Mapped[int] = mapped_column(ForeignKey("rhesus.id"))
    rhesus: Mapped["Rhesus"] = relationship(uselist=False, lazy="selectin")


class UsersConfig(Base):
    __tablename__ = "users_configs"
    extend_existing = True

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True, nullable=False)
    phone_number_status: Mapped[int] = mapped_column(Integer, index=True, nullable=False)
    social_networks_status: Mapped[int] = mapped_column(Integer, index=True, nullable=False)
    email_status: Mapped[int] = mapped_column(Integer, index=True, nullable=False)

    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"), nullable=False)
    user: Mapped["User"] = relationship(uselist=False, lazy="selectin")


class UserNetwork(Base):
    __tablename__ = "user_networks"
    extend_existing = True

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True, nullable=False)
    telegram: Mapped[str] = mapped_column(String)
    vk: Mapped[str] = mapped_column(String)


class Breed(Base):
    __tablename__ = "breeds"
    extend_existing = True

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True, nullable=False)
    title: Mapped[str] = mapped_column(String, unique=True, index=True, nullable=False)

    pet_type_id: Mapped[int] = mapped_column(ForeignKey("pet_types.id"), nullable=False)
    pet_type: Mapped["PetType"] = relationship(uselist=False, lazy="selectin")


class Demand(Base):
    __tablename__ = "demands"
    extend_existing = True

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True, nullable=False)

    reason: Mapped[str] = mapped_column(Text)

    blood_component_id: Mapped[int] = mapped_column(ForeignKey("blood_components.id"), nullable=False)
    blood_component: Mapped["BloodComponent"] = relationship(uselist=False, lazy="selectin")

    blood_amount: Mapped[int] = mapped_column(Integer, nullable=False)
    donor_amount: Mapped[int] = mapped_column(Integer, nullable=False)

    pet_id: Mapped[int] = mapped_column(ForeignKey("pets.id"), nullable=False)
    pet: Mapped["Pet"] = relationship(uselist=False, lazy="selectin")

    clinic_id: Mapped[int] = mapped_column(ForeignKey("clinics.id"), nullable=False)
    clinic: Mapped["Clinic"] = relationship(uselist=False, lazy="selectin")

    end_actual_date: Mapped[datetime.date] = mapped_column(nullable=False)


class Clinic(Base):
    __tablename__ = "clinics"
    extend_existing = True

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True, nullable=False)
    title: Mapped[str] = mapped_column(String, unique=True, index=True, nullable=False)
    address: Mapped[str] = mapped_column(String, unique=True, index=True, nullable=False)
    email: Mapped[str] = mapped_column(String, unique=True, index=True, nullable=False)
    phone: Mapped[str] = mapped_column(String, unique=True, index=True, nullable=False)

    city_id: Mapped[int] = mapped_column(ForeignKey("cities.id"), nullable=False)
    city: Mapped["City"] = relationship(uselist=False, lazy="selectin")
