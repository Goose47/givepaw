from pydantic import BaseModel


class AvatarCreate(BaseModel):
    id: int
    photo_path: str
    photo_thumb: str
