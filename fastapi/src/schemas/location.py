from pydantic import BaseModel


class Region(BaseModel):
    id: int
    title: str


class City(BaseModel):
    id: int
    title: str
    region: Region
