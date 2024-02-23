from pydantic import BaseModel


class PetType(BaseModel):
    id: int
    title: str
    icon: str
