from sqlalchemy.ext.asyncio import AsyncSession

from src.database.models import FilterType
from src.database.session_manager import db_manager
from src.repository.crud.base_crud_repository import SqlAlchemyRepository


class FilterTypeRepository(SqlAlchemyRepository):
    def __init__(self, session: AsyncSession):
        super().__init__(session)
        self.model = FilterType


filter_type_repository = FilterTypeRepository(db_manager.get_session)
