from http import HTTPStatus
from typing import List

from fastapi import APIRouter, HTTPException

from src.database.session_manager import db_manager
from src.repository.crud.base_crud_repository import SqlAlchemyRepository
from src.schemas import clinics_schemas as schemas
from src.database.models import associative as models

router = APIRouter(
    prefix="/cities",
    tags=["cities"],
)


@router.get('/', response_model=List[schemas.Clinic])
async def get_pet_types():
    try:
        clinics: List[models.Clinic] = await SqlAlchemyRepository(db_manager.get_session,
                                                                  model=models.Clinic).get_multi()

        return [schemas.Clinic(id=clinic.id,
                               addres=clinic.title,
                               phone=clinic.phone,
                               email=clinic.email,
                               city=schemas.City(id=clinic.city.id,
                                                 title=clinic.city.title,
                                                 region=schemas.Region(id=clinic.city.region.id,
                                                                       title=clinic.city.region.title))
                               ) for clinic in clinics]

    except Exception as e:
        raise HTTPException(status_code=HTTPStatus.IM_A_TEAPOT, detail={"cause": e.with_traceback})
