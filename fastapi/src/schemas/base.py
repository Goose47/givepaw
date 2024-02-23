import json

from pydantic import BaseModel, ConfigDict


class BaseSchema(BaseModel):
    class Config:
        arbitrary_types_allowed = True


class BaseResponseSchema:
    id: int

    def jsonify(self: BaseModel):
        return self.model_dump(mode="json")
