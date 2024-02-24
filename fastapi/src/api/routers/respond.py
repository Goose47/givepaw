from http import HTTPStatus
from typing import List

from fastapi import APIRouter, HTTPException

from src.database.models import many_to_many as models, create_donor_recipient
from src.database.session_manager import db_manager
from src.repository.crud.base_crud_repository import SqlAlchemyRepository
from src.schemas import donors
from src.schemas.donors import Donor
from src.schemas.location import create_city
from src.schemas.pets import create_pet
from src.schemas.recipients import create_recipient
import src.schemas.responds as schemas

router = APIRouter(
    prefix="/responds",
    tags=["responds"],
)


@router.get('/', response_model=list[schemas.DonorRecipient])
async def get_donor_recipient():
    all_responds: List[models.DonorRecipient] = await SqlAlchemyRepository(db_manager.get_session,
                                                                           model=models.DonorRecipient).get_multi(
        order="date")

    return [create_donor_recipient(respond) for respond in all_responds]
