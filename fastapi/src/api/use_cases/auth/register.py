from src.utils.crypt import Crypt
from src.schemas.auth import RegisterUser
from src.repository.crud.base_crud_repository import SqlAlchemyRepository
from src.database.session_manager import db_manager
from src.database.models.associative import User


class RegisterUseCase:
    @staticmethod
    async def register(data: RegisterUser) -> User:
        if await SqlAlchemyRepository(db_manager.get_session, model=User).get_single(username=data.username):
            raise Exception('This email is already taken')

        crypt = Crypt()

        hashed_password = crypt.hash(data.password)
        data.password = hashed_password

        user = await SqlAlchemyRepository(db_manager.get_session, model=User).create(data)

        return user
