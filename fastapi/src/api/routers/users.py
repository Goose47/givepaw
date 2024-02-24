from http import HTTPStatus

from fastapi import APIRouter, Depends, Request, HTTPException

from src.api.dependencies.auth import Auth
from src.database import models
from src.database.session_manager import db_manager
from src.repository.crud.base_crud_repository import SqlAlchemyRepository
from src.schemas import user
from src.schemas.location import create_city
from src.schemas.user import create_user_role, create_avatar, \
    create_user_network, create_user_config, UserUpdate, create_user

router = APIRouter(
    prefix="/users",
    tags=["users"],
)


@router.get('/user/info', response_model=user.UserProfile)
async def get_user_info(request: Request, auth: Auth = Depends()):
    try:
        await auth.check_access_token(request)
        user_id = request.state.user.id
        user_info: models.User = await SqlAlchemyRepository(db_manager.get_session, model=models.User).get_single(

            id=user_id)

        user_role = create_user_role(user_info.user_role)

        city = create_city(user_info.city)

        avatar = create_avatar(user_info.avatar)

        user_network = create_user_network(user_info.user_network)
        user_config = create_user_config(user_info.user_config)

        return user.UserProfile(id=user_info.id, surname=user_info.surname, name=user_info.name,
                                patronymic=user_info.patronymic, username=user_info.username,
                                email=user_info.email, user_role=user_role, city=city, avatar=avatar,
                                user_network=user_network, user_config=user_config)

    except Exception as e:
        raise HTTPException(status_code=HTTPStatus.BAD_REQUEST, detail=str(e))


@router.put("/user", response_model=user.UserProfile)
async def update_user(request: Request, data_user: UserUpdate, auth: Auth = Depends()):
    try:
        await auth.check_access_token(request)
        user: models.User = await SqlAlchemyRepository(db_manager.get_session,
                                                       model=models.User).get_single(id=request.state.user.id)
        if not user:
            raise Exception()

        user: models.User = await SqlAlchemyRepository(db_manager.get_session, model=models.User).update(data=data_user,
                                                                                                         id=request.state.user.id)
        user = create_user(user)
        return user

    except Exception as e:
        raise HTTPException(status_code=HTTPStatus.BAD_REQUEST, detail=str(e))


@router.put("/user/change_password", response_model=user.UserProfile)
async def update_user_password(request: Request, data_user: UserUpdate, auth: Auth = Depends()):
    try:
        await auth.check_access_token(request)
        user: models.User = await SqlAlchemyRepository(db_manager.get_session,
                                                       model=models.User).get_single(id=request.state.user.id)
        if not user:
            raise Exception()

        user: models.User = await SqlAlchemyRepository(db_manager.get_session, model=models.User).update(data=data_user,
                                                                                                         id=request.state.user.id)
        user = create_user(user)
        return user

    except Exception as e:
        raise HTTPException(status_code=HTTPStatus.BAD_REQUEST, detail=str(e))
