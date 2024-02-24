from pydantic import BaseModel


class Region(BaseModel):
    id: int
    title: str


def create_region(region):
    return Region(id=region.id, title=region.title)


class City(BaseModel):
    id: int
    title: str
    region: Region

class UpdateCity(BaseModel):
    title: str
    region_id: Region


def create_city(city):
    return City(id=city.id, title=city.title, region=create_region(city.region))
