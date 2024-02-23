from sqlalchemy.ext.asyncio import AsyncSession

from src.database.models import AdType
from src.database.session_manager import db_manager
from src.repository.crud.base_crud_repository import SqlAlchemyRepository


class AdTypeRepository(SqlAlchemyRepository):
    def __init__(self, session: AsyncSession):
        super().__init__(session)
        self.model = AdType


ad_type_repository = AdTypeRepository(db_manager.get_session)
