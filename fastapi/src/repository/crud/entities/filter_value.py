from sqlalchemy.ext.asyncio import AsyncSession

from src.database.models import FilterValue
from src.database.session_manager import db_manager
from src.repository.crud.base_crud_repository import SqlAlchemyRepository


class FilterValueRepository(SqlAlchemyRepository):
    def __init__(self, session: AsyncSession):
        super().__init__(session)
        self.model = FilterValue


filter_value_repository = FilterValueRepository(db_manager.get_session)
