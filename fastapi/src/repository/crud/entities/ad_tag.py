from sqlalchemy.ext.asyncio import AsyncSession

from src.database.models import AdTag
from src.database.session_manager import db_manager
from src.repository.crud.base_crud_repository import SqlAlchemyRepository


class AdTagRepository(SqlAlchemyRepository):
    def __init__(self, session: AsyncSession):
        super().__init__(session)
        self.model = AdTag


ad_tag_repository = AdTagRepository(db_manager.get_session)
