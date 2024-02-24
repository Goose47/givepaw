from http import HTTPStatus
from typing import List

from fastapi import APIRouter, HTTPException, Request, Depends
from src.api.dependencies.auth import Auth
from src.database.session_manager import db_manager
from src.repository.crud.base_crud_repository import SqlAlchemyRepository
from src.schemas import user_networks
from src.database.models.associative import UserNetwork
from src.schemas.user_networks import create_user_network

router = APIRouter(
    prefix="/user_networks",
    tags=["user_networks"],
)


@router.get('/', response_model=List[user_networks.UserNetwork])
async def index(request: Request, auth: Auth = Depends()):
    await auth.check_access_token(request)
    try:
        un_list: List[UserNetwork] = await SqlAlchemyRepository(db_manager.get_session, model=UserNetwork)\
            .get_multi(user_id=request.state.user.id)
        return [create_user_network(un) for un in un_list]
    except Exception as e:
        raise HTTPException(status_code=HTTPStatus.BAD_REQUEST, detail=str(e))


@router.post('/', response_model=user_networks.UserNetwork)
async def store(data: user_networks.UserNetworkCreate):
    try:
        recipient: UserNetwork = await SqlAlchemyRepository(db_manager.get_session, model=UserNetwork).create(data)
        return recipient

    except Exception as e:
        raise HTTPException(status_code=HTTPStatus.BAD_REQUEST, detail=str(e))


@router.put('/', response_model=user_networks.UserNetwork)
async def store(data: user_networks.UserNetworkUpdate):
    try:
        recipient: UserNetwork = await SqlAlchemyRepository(db_manager.get_session, model=UserNetwork).update(data, id=data.id)
        return recipient

    except Exception as e:
        raise HTTPException(status_code=HTTPStatus.BAD_REQUEST, detail=str(e))

