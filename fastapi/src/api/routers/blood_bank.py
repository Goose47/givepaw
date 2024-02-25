from http import HTTPStatus
from typing import List
from collections import Counter

from fastapi import APIRouter, HTTPException

from src.database.models import associative as models
from src.database.models import characteristics
from src.database.session_manager import db_manager
from src.repository.crud.base_crud_repository import SqlAlchemyRepository
from src.schemas import donors
from src.schemas.blood_group import PetBloodGroup, create_pet_blood_group
from src.schemas.clinics import Clinic, create_clinic
from src.schemas.donors import Donor
from src.schemas.location import create_city, City
from src.schemas.pets import create_pet
from src.schemas.recipients import create_recipient

router = APIRouter(
    prefix="/blood_bank",
    tags=["/blood_bank"],
)


@router.get('/min', response_model=PetBloodGroup)
async def get_min_of_blood_bank():
    try:
        donors_bloods: List[models.DonorBlood] = \
            await SqlAlchemyRepository(db_manager.get_session, model=models.DonorBlood).get_multi()

        bloods: List[models.PetBloodGroup] = \
            [donors_blood.donor.pet.blood_group for donors_blood in donors_bloods]

        counter = Counter(bloods)

        least_common: models.PetBloodGroup = counter.most_common()[-1][0]

        return create_pet_blood_group(least_common)


    except Exception as e:
        raise HTTPException(status_code=HTTPStatus.BAD_REQUEST, detail=str(e))
