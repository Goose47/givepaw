from sqlalchemy.ext.asyncio import AsyncSession

from src.database.models import UserRole
from src.database.session_manager import db_manager
from src.repository.crud.base_crud_repository import SqlAlchemyRepository


class UserRoleRepository(SqlAlchemyRepository):
    def __init__(self, session: AsyncSession):
        super().__init__(session)
        self.model = UserRole


user_role_repository = UserRoleRepository(db_manager.get_session)
