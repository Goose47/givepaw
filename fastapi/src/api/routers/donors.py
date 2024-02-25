from http import HTTPStatus
from typing import List

from fastapi import APIRouter, HTTPException

from src.database.models import associative as models
from src.database.session_manager import db_manager
from src.repository.crud.base_crud_repository import SqlAlchemyRepository
from src.schemas import donors
from src.schemas.clinics import Clinic, create_clinic
from src.schemas.donors import Donor
from src.schemas.location import create_city, City
from src.schemas.pets import create_pet
from src.schemas.recipients import create_recipient

router = APIRouter(
    prefix="/donors",
    tags=["donors"],
)


@router.get('/', response_model=List[donors.Donor])
async def index():
    try:
        all_donors: List[models.Donor] = await SqlAlchemyRepository(db_manager.get_session,
                                                                    model=models.Donor).get_multi()
        return [donors.Donor(
            id=donor.id,
            pet=create_pet(donor.pet),
            city=create_city(donor.city),
            recipient=create_recipient(donor.recipient) if donor.recipient else None)
            for donor in all_donors]

    except Exception as e:
        raise HTTPException(status_code=HTTPStatus.BAD_REQUEST, detail=str(e))


@router.post('/', response_model=donors.NewDonor)
async def store(data: donors.NewDonorCreate):
    try:
        old_donor = donors.DonorCreate(pet_id=data.pet_id,
                                       city_id=1,
                                       recipient_id=data.recipient_id if data.recipient_id else None
                                       )
        donor: models.Donor = await SqlAlchemyRepository(db_manager.get_session,
                                                         model=models.Donor).create(old_donor)

        clinic = create_clinic(await SqlAlchemyRepository(db_manager.get_session,
                                                          model=models.Clinic).get_single(id=data.clinic_id))

        return donors.NewDonor(id=donor.id,
                               pet=create_pet(donor.pet),
                               recipient=create_recipient(donor.recipient) if donor.recipient else None,
                               clinic=clinic,
                               date=data.date)

    except Exception as e:
        raise HTTPException(status_code=HTTPStatus.BAD_REQUEST, detail=str(e))


@router.get('/{user_id}', response_model=List[donors.Donor])
async def get_donors_by_user_id(user_id: int):
    try:
        all_donors: list[models.Donor] = await SqlAlchemyRepository(db_manager.get_session,
                                                                    model=models.Donor).get_multi()

        return [donors.Donor(id=donor.id,
                             pet=create_pet(donor.pet),
                             city=create_city(donor.city)
                             )
                for donor in all_donors if donor.pet.user_id == user_id]

    except Exception as e:
        raise HTTPException(status_code=HTTPStatus.BAD_REQUEST, detail=str(e))
