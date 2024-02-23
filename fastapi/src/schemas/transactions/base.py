from typing import ClassVar

from pydantic import BaseModel


class BaseTransaction(BaseModel):
    id: int
