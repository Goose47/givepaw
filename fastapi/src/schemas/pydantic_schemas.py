from pydantic import BaseModel


class PetType(BaseModel):
    id: int
    title: str
    icon: str


class Region(BaseModel):
    id: int
    title: str


class City(BaseModel):
    id: int
    title: str
    region: Region


class PetType(BaseModel):
    id: int
    title: str


class RhesusType(BaseModel):
    id: int
    title: str


class BloodGroup(BaseModel):
    id: int
    title: str


class PetBloodGroupSchema(BaseModel):
    id: int
    blood_group: BloodGroup
    pet_type: PetType
    rhesus_type: RhesusType

