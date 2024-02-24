from pydantic import BaseModel


class RhesusType(BaseModel):
    id: int
    title: str


class BloodGroup(BaseModel):
    id: int
    title: str


class PetBloodGroup(BaseModel):
    id: int
    blood_group: BloodGroup
    rhesus_type: RhesusType


class BloodComponent(BaseModel):
    id: int
    title: str
