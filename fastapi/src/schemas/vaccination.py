from pydantic import BaseModel


class Vaccination(BaseModel):
    id: int
    title: str
