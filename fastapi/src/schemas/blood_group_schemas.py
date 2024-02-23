from pydantic import BaseModel


class RhesusType(BaseModel):
    id: int
    title: str


class BloodGroup(BaseModel):
    id: int
    title: str


class PetBloodGroupSchema(BaseModel):
    id: int
    blood_group: BloodGroup
    rhesus_type: RhesusType
