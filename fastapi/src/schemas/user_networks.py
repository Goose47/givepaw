from typing import Optional

from pydantic import BaseModel


class UserNetwork(BaseModel):
    id: int
    telegram: Optional[str] = None
    vk: Optional[str] = None
class UserNetworkCreate(BaseModel):
    telegram: Optional[str] = None
    vk: Optional[str] = None
    user_id: Optional[int] = None
class UserNetworkUpdate(BaseModel):
    telegram: Optional[str] = None
    vk: Optional[str] = None


def create_user_network(un):
    return UserNetwork(
        id=un.id,
        telegram=un.telegram,
        vk=un.vk,
    )

