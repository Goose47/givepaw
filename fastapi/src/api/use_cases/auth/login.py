from src.database.models import User
from src.utils.crypt import Crypt
from src.utils.jwt.jwt_auth import JWT
from src.config.jwt.config import settings_jwt
from src.schemas.auth import LoginUser
from src.repository.crud.base_crud_repository import SqlAlchemyRepository
from src.database.session_manager import db_manager


class LoginUseCase:
    @staticmethod
    async def login(data: LoginUser):
        user = await LoginUseCase.authenticate_user(data.username, data.password)
        if not user:
            raise Exception("Incorrect username or password")

        jwt = JWT(settings_jwt)
        access_token = jwt.generate_access_token(data.email)
        refresh_token = jwt.generate_refresh_token(data.email)

        return access_token, refresh_token

    @staticmethod
    async def authenticate_user(username: str, password: str):
        user: User = await SqlAlchemyRepository(db_manager.get_session, model=User).get_single(username=username)
        if not user:
            return False
        crypt = Crypt()
        if not crypt.verify(password, user.password):
            return False
        return user
