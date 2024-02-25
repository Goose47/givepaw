from http import HTTPStatus
from typing import List
from collections import Counter

from fastapi import APIRouter, HTTPException

from src.database.models import associative as models
from src.database.models import characteristics
from src.database.session_manager import db_manager
from src.repository.crud.base_crud_repository import SqlAlchemyRepository
from src.schemas import donors
from src.schemas.blood_group import PetBloodGroup, create_pet_blood_group, create_pet_blood_group_for_bank, \
    PetBloodGroupForBank
from src.schemas.clinics import Clinic, create_clinic
from src.schemas.donors import Donor
from src.schemas.location import create_city, City
from src.schemas.pets import create_pet
from src.schemas.recipients import create_recipient

router = APIRouter(
    prefix="/blood_bank",
    tags=["/blood_bank"],
)


@router.get('/min', response_model=PetBloodGroupForBank)
async def get_min():
    try:
        donors_bloods: List[models.DonorBlood] = \
            await SqlAlchemyRepository(db_manager.get_session, model=models.DonorBlood).get_multi()

        bloods: List[tuple[models.PetBloodGroup, float]] = \
            [(donors_blood.donor.pet.blood_group, donors_blood.blood_amount) for donors_blood in donors_bloods]

        if not len(donors_bloods):
            raise HTTPException(status_code=HTTPStatus.IM_A_TEAPOT, detail="no blood")

        total_amount = dict()

        for blood in bloods:
            blood: tuple[models.PetBloodGroup, float]
            pet_blood_group_id = blood[0].id

            if pet_blood_group_id not in total_amount.keys():
                total_amount[pet_blood_group_id] = 0

            total_amount[pet_blood_group_id] += blood[1]

        min_id = min(total_amount.items(), key=lambda x: x[1])
        raise HTTPException(detail=min_id)
        res = [blood for blood in bloods if blood[0].id == min_id]

        return create_pet_blood_group_for_bank(res)


    except Exception as e:
        raise HTTPException(status_code=HTTPStatus.BAD_REQUEST, detail=str(e))


@router.get("/necessary", response_model=PetBloodGroupForBank)
async def get_the_most_necessary():
    try:
        all_recipients: List[models.Recipient] = \
            await SqlAlchemyRepository(db_manager.get_session, model=models.Recipient).get_multi()

        bloods: List[models.PetBloodGroup] = [rec.pet.blood_group for rec in all_recipients]

        counter = Counter(bloods)

        least_common: models.PetBloodGroup = counter.most_common()[0][0]

        return create_pet_blood_group_for_bank(least_common)


    except Exception as e:
        raise HTTPException(status_code=HTTPStatus.BAD_REQUEST, detail=str(e))
