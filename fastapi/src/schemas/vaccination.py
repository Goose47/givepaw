from pydantic import BaseModel


class Vaccination(BaseModel):
    id: int
    title: str


def create_vaccination(vaccination):
    return Vaccination(id=vaccination.id, title=vaccination.title)


def create_vaccinations(vaccinations):
    return [create_vaccination(v) for v in vaccinations]
