from http import HTTPStatus
from typing import List

from fastapi import APIRouter, HTTPException, Request, Depends

from src.database.session_manager import db_manager
from src.repository.crud.base_crud_repository import SqlAlchemyRepository

from src.schemas import pets, vaccination, breed, blood_group
from src.database import models
from src.schemas.blood_group import create_blood_component
from src.schemas.pets import Pet

from src.api.dependencies.auth import Auth

router = APIRouter(
    prefix="/pets",
    tags=["pets"],
)


@router.get('/pet_types', response_model=List[pets.PetType])
async def get_pet_types():
    try:
        types: List[models.PetType] = await SqlAlchemyRepository(db_manager.get_session,
                                                                 model=models.PetType).get_multi()

        return [pets.PetType(id=t.id,
                             title=t.title,
                             icon=t.link) for t in types]

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


@router.get('/blood_components', response_model=List[blood_group.BloodComponent])
async def get_blood_components():
    try:
        components: List[models.BloodComponent] = await SqlAlchemyRepository(db_manager.get_session,
                                                                             model=models.BloodComponent).get_multi()

        return [create_blood_component(c) for c in components]

    except Exception as e:
        raise HTTPException(status_code=HTTPStatus.IM_A_TEAPOT, detail={"cause": "Artem"})


@router.get('/my', response_model=List[Pet])
async def get_my(request: Request, auth: Auth = Depends()):
    await auth.check_access_token(request)
    try:
        pets: List[models.Pet] = await SqlAlchemyRepository(db_manager.get_session, model=models.Pet) \
            .get_multi(user_id=request.state.user.id)
        return pets

    except Exception as e:
        raise HTTPException(status_code=HTTPStatus.BAD_REQUEST, detail=str(e))


@router.post('/', response_model=Pet)
async def create_pet(new_pet: Pet):
    try:
        added_pet: models.Pet = await SqlAlchemyRepository(db_manager.get_session, model=models.Pet).create(new_pet)
        return added_pet
    except Exception as e:
        raise HTTPException(status_code=HTTPStatus.BAD_REQUEST, detail=str(e))

