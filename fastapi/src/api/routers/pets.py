from http import HTTPStatus
from typing import List, Dict

from fastapi import APIRouter, HTTPException

from src.database.session_manager import db_manager
from src.repository.crud.base_crud_repository import SqlAlchemyRepository
from src.schemas import characteristics as schemas
from src.database.models import characteristics as models
from src.schemas.characteristics import PetType

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
