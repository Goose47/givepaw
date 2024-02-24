from http import HTTPStatus
from typing import List

from fastapi import APIRouter, HTTPException

from src.database.models import associative as schema
from src.database.session_manager import db_manager
from src.repository.crud.base_crud_repository import SqlAlchemyRepository
from src.schemas import donors
from src.database import models
from src.schemas.donors import Donor
from src.schemas.location import create_city
from src.schemas.pets import create_pet

router = APIRouter(
    prefix="/donors",
    tags=["donors"],
)


@router.get('/', response_model=List[donors.Donor])
async def index():
    try:
        donors: List[models.Donor] = await SqlAlchemyRepository(db_manager.get_session, model=Donor).get_multi()
        return donors

    except Exception as e:
        raise HTTPException(status_code=HTTPStatus.BAD_REQUEST, detail=str(e))


@router.post('/', response_model=donors.Donor)
async def store(data: donors.DonorCreate):
    try:
        donor: models.Donor = await SqlAlchemyRepository(db_manager.get_session, model=schema.Donor).create(data)

        return donors.Donor(id=donor.id, pet=create_pet(donor.pet), city=create_city(donor.city))

    except Exception as e:
        raise HTTPException(status_code=HTTPStatus.BAD_REQUEST, detail=str(e))


@router.get('/by_user_id', response_model=list[schema.Donor])
async def get_donors_by_user_id(user_id: int):
    try:
        all_donors: list[schema.Donor] = await SqlAlchemyRepository(db_manager.get_session,
                                                                    model=schema.Donor).get_multi()

        return [donors.Donor(id=donor.id,
                             pet=create_pet(donor.pet),
                             city=create_city(donor.city)
                             )
                for donor in all_donors if donor.pet.user_id == user_id]

    except Exception as e:
        raise HTTPException(status_code=HTTPStatus.BAD_REQUEST, detail=str(e))
