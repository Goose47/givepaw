from pydantic import BaseModel


class PetType(BaseModel):
    id: int
    title: str

    def jsonify(self: BaseModel):
        return self.model_dump(mode="json")
