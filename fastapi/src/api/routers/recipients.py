from http import HTTPStatus
from typing import List

from fastapi import APIRouter, HTTPException

from src.database.session_manager import db_manager
from src.repository.crud.base_crud_repository import SqlAlchemyRepository
from src.schemas import recipients
from src.database.models.associative import Recipient

router = APIRouter(
    prefix="/recipients",
    tags=["recipients"],
)


@router.get('/', response_model=List[recipients.Recipient])
async def index():
    try:
        recipients: List[Recipient] = await SqlAlchemyRepository(db_manager.get_session, model=Recipient).get_multi()
        return recipients

    except Exception as e:
        raise HTTPException(status_code=HTTPStatus.BAD_REQUEST, detail=str(e))


@router.post('/', response_model=recipients.Recipient)
async def store(data: recipients.RecipientCreate):
    try:
        recipient: Recipient = await SqlAlchemyRepository(db_manager.get_session, model=Recipient).create(data)
        return recipient

    except Exception as e:
        raise HTTPException(status_code=HTTPStatus.BAD_REQUEST, detail=str(e))
