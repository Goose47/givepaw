from http import HTTPStatus
from typing import List

from fastapi import APIRouter, HTTPException, Request, Depends

from src.database.session_manager import db_manager
from src.repository.crud.base_crud_repository import SqlAlchemyRepository

from src.schemas import pet_type, vaccination, breed,
from src.database import models
from src.schemas.pets import PetViewType

from src.api.dependencies.auth import Auth

router = APIRouter(
    prefix="/pets",
    tags=["pets"],
)


@router.get('/pet_types', response_model=List[pet_type.PetType])
async def get_pet_types():
    try:
        types: List[models.PetType] = await SqlAlchemyRepository(db_manager.get_session,
                                                                 model=models.PetType).get_multi()

        return [pet_type.PetType(id=t.id,
                                 title=t.title,
                                 icon=t.icon) for t in types]

    except Exception as e:
        raise HTTPException(status_code=HTTPStatus.IM_A_TEAPOT, detail={"cause": "Artem"})


@router.get('/vaccinations', response_model=List[vaccination.Vaccination])
async def get_vaccinations():
    try:
        vaccinations: List[models.Vaccination] = await SqlAlchemyRepository(db_manager.get_session,
                                                                            model=models.Vaccination).get_multi()

        return [vaccination.Vaccination(id=v.id,
                                        title=v.title) for v in vaccinations]

    except Exception as e:
        raise HTTPException(status_code=HTTPStatus.IM_A_TEAPOT, detail={"cause": "Artem"})


@router.get('/breeds/{pet_type_id}', response_model=List[breed.BreedResponse])
async def get_breeds(pet_type_id: int):
    try:
        breeds: List[models.Breed] = await SqlAlchemyRepository(db_manager.get_session,
                                                                model=models.Breed).get_multi(pet_type_id=pet_type_id)

        return [breed.BreedResponse(id=v.id, title=v.title) for v in breeds]

    except Exception as e:
        raise HTTPException(status_code=HTTPStatus.IM_A_TEAPOT, detail={"cause": "Artem"})


@router.get('/my', response_model=List[PetViewType])
async def get_my(request: Request, auth: Auth = Depends()):
    await auth.check_access_token(request)
    try:
        pets: List[models.Pet] = await SqlAlchemyRepository(db_manager.get_session, model=models.Pet)\
            .get_multi(user_id=request.state.user.id)
        return pets

    except Exception as e:
        raise HTTPException(status_code=HTTPStatus.BAD_REQUEST, detail=str(e))


@router.post('/')
async def create_pet(request: Request):
    try:

