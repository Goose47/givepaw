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




