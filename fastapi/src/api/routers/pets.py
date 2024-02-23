from typing import List

from fastapi import APIRouter

from src.api.responses.api_response import ApiResponse
from src.database.session_manager import db_manager
from src.repository.crud.base_crud_repository import SqlAlchemyRepository
from src.schemas import characteristics as schemas
from src.database.models import characteristics as models

router = APIRouter(
    prefix="/pets",
    tags=["pets"],
)


@router.get('/pet_types', response_model=ApiResponse)
async def get_pet_types():
    try:
        types: List[models.PetType] = await SqlAlchemyRepository(db_manager.get_session,
                                                                 model=models.PetType).get_multi()
        types: List[schemas.PetType] = [schemas.PetType(id=type.id, title=type.title) for type in types]
    except Exception as e:
        return ApiResponse.error(str(e))
    return ApiResponse.payload({
        'types': types,
    })
