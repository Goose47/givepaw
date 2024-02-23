from sqlalchemy.ext.asyncio import AsyncSession

from src.database.models import Filter
from src.database.session_manager import db_manager
from src.repository.crud.base_crud_repository import SqlAlchemyRepository


class FilterRepository(SqlAlchemyRepository):
    def __init__(self, session: AsyncSession):
        super().__init__(session)
        self.model = Filter


filter_repository = FilterRepository(db_manager.get_session)
