from sqlalchemy.ext.asyncio import AsyncSession

from src.database.models import AdPriority
from src.database.session_manager import db_manager
from src.repository.crud.base_crud_repository import SqlAlchemyRepository


class AdPriorityRepository(SqlAlchemyRepository):
    def __init__(self, session: AsyncSession):
        super().__init__(session)
        self.model = AdPriority


ad_priority_repository = AdPriorityRepository(db_manager.get_session)
