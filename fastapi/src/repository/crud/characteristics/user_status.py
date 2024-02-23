from sqlalchemy.ext.asyncio import AsyncSession

from src.database.models import UserStatus
from src.database.session_manager import db_manager
from src.repository.crud.base_crud_repository import SqlAlchemyRepository


class UserStatusRepository(SqlAlchemyRepository):
    def __init__(self, session: AsyncSession):
        super().__init__(session)
        self.model = UserStatus


user_status_repository = UserStatusRepository(db_manager.get_session)
