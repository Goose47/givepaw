from pydantic import BaseModel


class Rhesus(BaseModel):
    id: int
    title: str


def create_rhesus_type(rhesus):
    return Rhesus(id=rhesus.id, title=rhesus.title)


class BloodGroup(BaseModel):
    id: int
    title: str


def create_blood_group(blood):
    return BloodGroup(id=blood.id, title=blood.title)


class PetBloodGroup(BaseModel):
    id: int
    blood_group: BloodGroup
    rhesus: Rhesus


def create_pet_blood_group(pet_blood_group):
    return PetBloodGroup(id=pet_blood_group.id, blood_group=pet_blood_group.blood_group,
                         rhesus=create_rhesus_type(pet_blood_group.rhesus))


class BloodComponent(BaseModel):
    id: int
    title: str


def create_blood_component(blood_component):
    return BloodComponent(id=blood_component.id, title=blood_component.title)
