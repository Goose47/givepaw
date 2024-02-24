from pydantic import BaseModel


class AvatarCreate(BaseModel):
    photo_path: str
    photo_thumb: str
