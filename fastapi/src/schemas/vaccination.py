import datetime

from pydantic import BaseModel


class Vaccination(BaseModel):
    id: int
    title: str


class PetVaccinationCreate(BaseModel):
    vaccination_id: int
    date: datetime.date


class PetVaccination(BaseModel):
    vaccination_id: int
    pet_id: int
    date: datetime.date


def create_vaccination(vaccination):
    return Vaccination(id=vaccination.id, title=vaccination.title)


def create_vaccinations(vaccinations):
    return [create_vaccination(v) for v in vaccinations]
