from http import HTTPStatus
from typing import List

from fastapi import APIRouter, HTTPException

from src.database.session_manager import db_manager
from src.repository.crud.base_crud_repository import SqlAlchemyRepository
from src.schemas.donors import DonorCreateType, DonorViewType
from src.database.models.associative import Donor

router = APIRouter(
    prefix="/donors",
    tags=["donors"],
)


@router.get('/', response_model=List[DonorViewType])
async def index():
    try:
        donors: List[Donor] = await SqlAlchemyRepository(db_manager.get_session, model=Donor).get_multi()
        return donors

    except Exception as e:
        raise HTTPException(status_code=HTTPStatus.BAD_REQUEST, detail=str(e))


@router.post('/', response_model=DonorViewType)
async def store(data: DonorCreateType):
    try:
        donor: Donor = await SqlAlchemyRepository(db_manager.get_session, model=Donor).create(data)
        return donor

    except Exception as e:
        raise HTTPException(status_code=HTTPStatus.BAD_REQUEST, detail=str(e))
