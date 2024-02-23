from http import HTTPStatus
from typing import List

from fastapi import APIRouter, HTTPException

from src.database.session_manager import db_manager
from src.repository.crud.base_crud_repository import SqlAlchemyRepository
from src.schemas import pydantic_schemas as schemas
from src.database.models import characteristics as models

router = APIRouter(
    prefix="/pets",
    tags=["pets"],
)


@router.get('/pet_types', response_model=List[schemas.PetType])
async def get_pet_types():
    try:
        types: List[models.PetType] = await SqlAlchemyRepository(db_manager.get_session,
                                                                 model=models.PetType).get_multi()

        return [schemas.PetType(id=t.id,
                                title=t.title,
                                icon=t.icon) for t in types]

    except Exception as e:
        raise HTTPException(status_code=HTTPStatus.IM_A_TEAPOT, detail={"cause": "Artem"})


@router.get('/vaccinations', response_model=List[schemas.Vaccination])
async def get_vaccinations():
    try:
        vaccinations: List[models.Vaccination] = await SqlAlchemyRepository(db_manager.get_session,
                                                                            model=models.Vaccination).get_multi()

        return [schemas.Vaccination(id=v.id,
                                    title=v.title) for v in vaccinations]

    except Exception as e:
        raise HTTPException(status_code=HTTPStatus.IM_A_TEAPOT, detail={"cause": "Artem"})


@router.get('/breeds', response_model=List[schemas.Breed])
async def get_breeds():
    try:
        breeds: List[models.Breed] = await SqlAlchemyRepository(db_manager.get_session,
                                                                model=models.Breed).get_multi()

        return [schemas.Breed(id=v.id,
                              title=v.title) for v in breeds]

    except Exception as e:
        raise HTTPException(status_code=HTTPStatus.IM_A_TEAPOT, detail={"cause": "Artem"})
