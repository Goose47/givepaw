from src.utils.crypt import Crypt
from src.schemas.auth import RegisterUser, UserType
from src.schemas.user import UserConfigCreateType, UserNetworksCreateType
from src.schemas.avatars import AvatarCreate
from src.repository.crud.base_crud_repository import SqlAlchemyRepository
from src.database.session_manager import db_manager
from src.database.models.associative import User, UserConfig, UserNetwork
from src.database.models.characteristics import Avatar
from fastapi import UploadFile, HTTPException
from src.utils.storage import Storage
from typing import Optional
from http import HTTPStatus


class RegisterUseCase:
    @staticmethod
    async def register(data: RegisterUser) -> UserType:
        if await SqlAlchemyRepository(db_manager.get_session, model=User).get_single(username=data.username):
            raise Exception('This username is already taken')
        if await SqlAlchemyRepository(db_manager.get_session, model=User).get_single(email=data.email):
            raise Exception('This email is already taken')

        crypt = Crypt()

        hashed_password = crypt.hash(data.password)
        # data.user_role_id = 1  # todo enum

        avatar = None
        if data.avatar:
            storage = Storage()
            try:
                path = storage.save_from_base64(data.avatar, 'avatars')
            except Exception as e:
                raise HTTPException(status_code=HTTPStatus.BAD_REQUEST, detail='Wrong image format')
            avatar = await SqlAlchemyRepository(db_manager.get_session, model=Avatar) \
                .create(AvatarCreate(photo_path=path, photo_thumb=path))

        user = await SqlAlchemyRepository(db_manager.get_session, model=User).create(RegisterUser(
            username=data.username,
            name=data.name,
            surname=data.surname,
            patronymic=data.patronymic,
            email=data.email,
            password=hashed_password,
            city_id=data.city_id,
            avatar_id=avatar.id if avatar else None,
            user_role_id=1,
        ))
        await SqlAlchemyRepository(db_manager.get_session, model=UserConfig)\
            .create(UserConfigCreateType(user_id=user.id))
        await SqlAlchemyRepository(db_manager.get_session, model=UserNetwork)\
            .create(UserNetworksCreateType(user_id=user.id))

        return UserType(
            id=user.id,
            username=user.username,
            name=user.name,
            surname=user.surname,
            patronymic=user.patronymic,
            email=user.email,
            user_role_id=user.user_role_id,
            city_id=user.city_id,
            avatar_id=avatar.id if avatar else None,
            avatar_link=user.avatar_link,
        )
