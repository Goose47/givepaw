from http import HTTPStatus
from typing import List

from fastapi import APIRouter, HTTPException, Request

from src.database.session_manager import db_manager
from src.repository.crud.base_crud_repository import SqlAlchemyRepository
from src.schemas import location as schemas
from src.database.models import associative as models
from src.schemas.location import UpdateCity, create_city

router = APIRouter(
    prefix="/cities",
    tags=["cities"],
)


@router.get('/', response_model=List[schemas.City])
async def get_cities():
    try:
        types: List[models.City] = await SqlAlchemyRepository(db_manager.get_session,
                                                              model=models.City).get_multi()

        return [schemas.City(id=t.id,
                             title=t.title,
                             region=schemas.Region(id=t.region.id,
                                                   title=t.region.title)
                             ) for t in types]

    except Exception as e:
        raise HTTPException(status_code=HTTPStatus.IM_A_TEAPOT, detail={"cause": e.with_traceback})


@router.put('/{city_id}', response_model=schemas.City)
async def update_city(city_id: int, request: Request, data_city: UpdateCity):
    try:
        city: models.City = await SqlAlchemyRepository(db_manager.get_session,
                                                       model=models.City).get_single(id=city_id)
        if not city:
            raise Exception("Город с данным id не найден.")

        city = await SqlAlchemyRepository(db_manager.get_session, model=models.City).update(data_city, id=city_ids)
        return create_city(city)

    except Exception as e:
        raise HTTPException(status_code=HTTPStatus.BAD_REQUEST, detail=str(e))
