from pydantic import BaseModel


class PetType(BaseModel):
    id: int
    title: str
    icon: str

    @property
    def link(self):
        return self.icon + 'jajajaja'


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


class PetBloodGroupForBank(BaseModel):
    id: int
    blood_group: BloodGroup
    rhesus: Rhesus
    pet_type: PetType


def create_pet_blood_group(pet_blood_group):
    return PetBloodGroup(id=pet_blood_group.id,
                         blood_group=create_blood_group(
                             pet_blood_group.blood_group) if pet_blood_group.blood_group else None,
                         rhesus=create_rhesus_type(pet_blood_group.rhesus) if pet_blood_group.rhesus else None)


def create_pet_blood_group_for_bank(pet_blood_group):
    return PetBloodGroupForBank(id=pet_blood_group.id,
                                blood_group=create_blood_group(
                                    pet_blood_group.blood_group) if pet_blood_group.blood_group else None,
                                rhesus=create_rhesus_type(pet_blood_group.rhesus) if pet_blood_group.rhesus else None,
                                pet_type=PetType(id=pet_blood_group.pet_type.id,
                                                 title=pet_blood_group.pet_type.title,
                                                 icon=pet_blood_group.pet_type.icon))


class BloodComponent(BaseModel):
    id: int
    title: str


def create_blood_component(blood_component):
    return BloodComponent(id=blood_component.id, title=blood_component.title)
