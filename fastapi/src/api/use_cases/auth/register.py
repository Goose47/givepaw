from src.utils.crypt import Crypt
from src.schemas.auth import RegisterUser, UserType
from src.repository.crud.base_crud_repository import SqlAlchemyRepository
from src.database.session_manager import db_manager
from src.database.models.associative import User


class RegisterUseCase:
    @staticmethod
    async def register(data: RegisterUser) -> UserType:
        if await SqlAlchemyRepository(db_manager.get_session, model=User).get_single(username=data.username):
            raise Exception('This username is already taken')
        if await SqlAlchemyRepository(db_manager.get_session, model=User).get_single(email=data.email):
            raise Exception('This email is already taken')

        crypt = Crypt()

        hashed_password = crypt.hash(data.password)
        data.password = hashed_password
        data.user_role_id = 1  # todo enum

        user = await SqlAlchemyRepository(db_manager.get_session, model=User).create(data)
        return UserType(
            id=user.id,
            username=user.username,
            name=user.name,
            surname=user.surname,
            patronymic=user.patronymic,
            email=user.email,
            user_role_id=user.user_role_id,
            city_id=user.city_id,
            avatar_id=user.avatar_id
        )
