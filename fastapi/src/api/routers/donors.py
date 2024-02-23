from http import HTTPStatus
from typing import List

from fastapi import APIRouter, HTTPException

from src.database.session_manager import db_manager
from src.repository.crud.base_crud_repository import SqlAlchemyRepository
from src.schemas import donors
from src.database import models
from src.schemas.donors import Donor

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
        donor: models.Donor = await SqlAlchemyRepository(db_manager.get_session, model=donors.Donor).create(data)
        return donor

    except Exception as e:
        raise HTTPException(status_code=HTTPStatus.BAD_REQUEST, detail=str(e))
