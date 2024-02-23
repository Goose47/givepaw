from sqlalchemy.ext.asyncio import AsyncSession

from src.database.models import UserField
from src.database.session_manager import db_manager
from src.repository.crud.base_crud_repository import SqlAlchemyRepository


class UserFieldRepository(SqlAlchemyRepository):
    def __init__(self, session: AsyncSession):
        super().__init__(session)
        self.model = UserField


user_field_repository = UserFieldRepository(db_manager.get_session)
