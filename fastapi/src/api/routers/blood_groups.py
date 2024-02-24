import random
from http import HTTPStatus
from typing import List

from fastapi import APIRouter, Request, HTTPException
import src.schemas.blood_group as schemas
import src.database.models.associative as models
from src.database.session_manager import db_manager
from src.repository.crud.base_crud_repository import SqlAlchemyRepository

router = APIRouter(
    prefix="/blood_group",
    tags=["blood_group"],
)


@router.get(
    "/{pet_type_id}", response_model=list[schemas.PetBloodGroup]
)
async def get_blood_group(request: Request, pet_type_id: int):
    try:
        blood_groups: List[models.PetBloodGroup] = await SqlAlchemyRepository(
            db_manager.get_session, model=models.PetBloodGroup
        ).get_multi(pet_type_id=pet_type_id)
        return [
            schemas.PetBloodGroup(
                id=pet_blood_group.id,
                blood_group=schemas.BloodGroup(
                    id=pet_blood_group.blood_group.id, title=pet_blood_group.blood_group.title
                ),
                rhesus_type=schemas.RhesusType(
                    id=pet_blood_group.rhesus.id, title=pet_blood_group.rhesus.title
                ),
            )
            for pet_blood_group in blood_groups
        ]

    except Exception as e:
        raise Exception
