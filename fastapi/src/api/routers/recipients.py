from http import HTTPStatus
from typing import List

from fastapi import APIRouter, HTTPException

from src.database.session_manager import db_manager
from src.repository.crud.base_crud_repository import SqlAlchemyRepository
from src.schemas import recipients
from src.database.models.associative import Recipient
from src.schemas.blood_group import BloodComponent

router = APIRouter(
    prefix="/recipients",
    tags=["recipients"],
)


@router.get('/', response_model=List[recipients.Recipient])
async def index():
    try:
        recipient_list: List[Recipient] = await SqlAlchemyRepository(db_manager.get_session,
                                                                     model=Recipient).get_multi()
        return [recipients.Recipient(id=r.id, reason=r.reason, blood_component=BloodComponent(id=r.blood_component.id,
                                                                                              title=r.blood_component.title),
                                     blood_amount=r.blood_amount, donor_amount=r.donor_amount, pet=Pet(r.pet.id)) for r in recipient_list]
    id: int

    reason: str
    blood_component: BloodComponent
    blood_amount: int
    donor_amount: int
    pet: Pet
    clinic_id: Clinic
    end_actual_date: datetime.date
    except Exception as e:
    raise HTTPException(status_code=HTTPStatus.BAD_REQUEST, detail=str(e))


@router.post('/', response_model=recipients.Recipient)
async def store(data: recipients.RecipientCreate):
    try:
        recipient: Recipient = await SqlAlchemyRepository(db_manager.get_session, model=Recipient).create(data)
        return recipient

    except Exception as e:
        raise HTTPException(status_code=HTTPStatus.BAD_REQUEST, detail=str(e))
