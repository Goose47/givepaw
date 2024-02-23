import random
from fastapi import APIRouter, Request

from pydantic import BaseModel

router = APIRouter(
    prefix="/mock",
    tags=["mocks"],
)


class MockPetType(BaseModel):
    id: int
    title: str


class MockRhesusType(BaseModel):
    id: int
    title: str


class MockBloodGroup(BaseModel):
    id: int
    title: str


class MockPetBloodGroupSchema(BaseModel):
    id: int
    blood_group: MockBloodGroup
    rhesus_type: MockRhesusType


@router.get("/pet_blood_group/{animal_type}", response_model=list[MockPetBloodGroupSchema])
async def mock_blood_group(request: Request, animal_type: str):
    return [MockPetBloodGroupSchema(
        id=random.randint(1, 100),
        blood_group=MockBloodGroup(id=random.randint(1, 100), title=random.choice(["I", "II", "III"])),
        rhesus_type=MockRhesusType(id=random.randint(1, 100), title=random.choice([
            f"фактор {animal_type} 1",
            f"фактор {animal_type} 2",
            f"фактор {animal_type} 3"
        ]))
    ) for _ in range(10)]
