import datetime
import locale
from http import HTTPStatus
from typing import List, Optional

from fastapi import APIRouter, HTTPException

from src.database.session_manager import db_manager
from src.repository.crud.base_crud_repository import SqlAlchemyRepository
from src.schemas import recipients
import src.database.models.associative as model
from src.schemas.blood_group import BloodComponent
from src.schemas.recipients import create_recipient, RecipientFilter

router = APIRouter(
    prefix="/recipients",
    tags=["recipients"],
)

months_dict = {
    'January': 'Января',
    'February': 'Февраля',
    'March': 'Марта',
    'April': 'Апреля',
    'May': 'Мая',
    'June': 'Июня',
    'July': 'Июля',
    'August': 'Августа',
    'September': 'Сентября',
    'October': 'Октября',
    'November': 'Ноября',
    'December': 'Декабря'
}


@router.get('/', response_model=List[recipients.Recipient])
async def index():
    # try:
    recipient_list: List[model.Recipient] = await SqlAlchemyRepository(db_manager.get_session,
                                                                       model=model.Recipient).get_multi()
    return [create_recipient(r) for r in recipient_list]

    # except Exception as e:
    # raise HTTPException(status_code=HTTPStatus.BAD_REQUEST, detail=str(e))


@router.post('/', response_model=recipients.Recipient)
async def store(data: recipients.RecipientCreate):
    try:
        recipient: model.Recipient = await SqlAlchemyRepository(db_manager.get_session, model=model.Recipient).create(
            data)
        return recipient

    except Exception as e:
        raise HTTPException(status_code=HTTPStatus.BAD_REQUEST, detail=str(e))


@router.post('/sort_by_data', response_model=list[recipients.RecipientForSortByData])
async def sort_recep_by_data(rec_filter: Optional[RecipientFilter] =
                             RecipientFilter(animal_type=None, breed=None, city=None, offset=None)):
    locale.setlocale(locale.LC_TIME, 'ru_RU')

    try:
        recipient: list[model.Recipient] = await SqlAlchemyRepository(
            db_manager.get_session,
            model=model.Recipient).get_multi()

        result = [
                     recipients.RecipientForSortByData(
                         id=rec.id,
                         avatar=rec.pet.avatar.photo_path,
                         name=rec.pet.name,
                         blood_group=rec.pet.blood_group.blood_group.title,
                         place=rec.clinic.address,
                         deadline=f"До {rec.end_actual_date.strftime('%d')} {months_dict[rec.end_actual_date.strftime('%B')]}",
                         reason=rec.reason,
                         number_required=rec.donor_amount
                     ) for rec in recipient

                     if (rec.end_actual_date >= datetime.date.today() and
                         bool(rec.pet.pet_type.id == rec_filter.animal_type if rec_filter.animal_type else True) and
                         bool(rec.pet.breed_id == rec_filter.breed if rec_filter.breed else True) and
                         bool(rec.clinic.city.id == rec_filter.city if rec_filter.city else True)
                         )
                 ][::-1]

        if rec_filter.offset:
            return result[:rec_filter.offset]

        return result

    except Exception as e:
        raise e


@router.get('/{user_id}', response_model=list[recipients.Recipient])
async def get_recipients_by_user_id(user_id: int):
    try:
        all_recipients: list[model.Recipient] = await SqlAlchemyRepository(db_manager.get_session,
                                                                           model=model.Recipient).get_multi()

        return [create_recipient(rec) for rec in all_recipients if rec.pet.user_id == user_id]

    except Exception as e:
        raise HTTPException(status_code=HTTPStatus.BAD_REQUEST, detail=str(e))
