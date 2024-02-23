from http import HTTPStatus
from typing import List

from fastapi import APIRouter, HTTPException

from src.database.session_manager import db_manager
from src.repository.crud.base_crud_repository import SqlAlchemyRepository
from src.schemas import pydantic_schemas as schemas
from src.database.models import associative as models

router = APIRouter(
    prefix="/cities",
    tags=["cities"],
)


@router.get('/cities', response_model=List[schemas.City])
async def get_pet_types():
    try:
        types: List[models.City] = await SqlAlchemyRepository(db_manager.get_session,
                                                              model=models.City).get_multi()

        return [schemas.City(id=t.id, title=t.title, region=t.region) for t in types]

    except Exception as e:
        raise HTTPException(status_code=HTTPStatus.IM_A_TEAPOT, detail={"cause": e.with_traceback()})
