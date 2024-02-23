from http import HTTPStatus
from typing import List

from fastapi import APIRouter, HTTPException

from src.database.session_manager import db_manager
from src.repository.crud.base_crud_repository import SqlAlchemyRepository
from src.schemas.recipients import RecipientViewType, RecipientCreateType
from src.database.models.associative import Recipient

router = APIRouter(
    prefix="/recipients",
    tags=["recipients"],
)


@router.get('/', response_model=List[RecipientViewType])
async def index():
    try:
        recipients: List[Recipient] = await SqlAlchemyRepository(db_manager.get_session, model=Recipient).get_multi()
        return recipients

    except Exception as e:
        raise HTTPException(status_code=HTTPStatus.BAD_REQUEST, detail=str(e))


@router.post('/', response_model=RecipientViewType)
async def store(data: RecipientCreateType):
    try:
        recipient: Recipient = await SqlAlchemyRepository(db_manager.get_session, model=Recipient).create(data)
        return recipient  # todo test
        return RecipientViewType(
            id=recipient.id,
            reason=recipient.reason,
            blood_component_id=recipient.blood_component_id,
            blood_amount=recipient.blood_amount,
            donor_amount=recipient.donor_amount,
            pet_id=recipient.pet_id,
            clinic_id=recipient.clinic_id,
            end_actual_date=recipient.end_actual_date,
        )

    except Exception as e:
        raise HTTPException(status_code=HTTPStatus.BAD_REQUEST, detail=str(e))
