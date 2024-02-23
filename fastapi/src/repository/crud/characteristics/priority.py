from sqlalchemy.ext.asyncio import AsyncSession

from src.database.models import Priority
from src.database.session_manager import db_manager
from src.repository.crud.base_crud_repository import SqlAlchemyRepository


class PriorityRepository(SqlAlchemyRepository):
    def __init__(self, session: AsyncSession):
        super().__init__(session)
        self.model = Priority


priority_repository = PriorityRepository(db_manager.get_session)
