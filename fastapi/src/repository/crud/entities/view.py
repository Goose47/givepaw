from sqlalchemy.ext.asyncio import AsyncSession

from src.database.models import View
from src.database.session_manager import db_manager
from src.repository.crud.base_crud_repository import SqlAlchemyRepository


class ViewRepository(SqlAlchemyRepository):
    def __init__(self, session: AsyncSession):
        super().__init__(session)
        self.model = View


view_repository = ViewRepository(db_manager.get_session)
