from sqlalchemy.ext.asyncio import AsyncSession

from src.database.models import Country
from src.database.session_manager import db_manager
from src.repository.crud.base_crud_repository import SqlAlchemyRepository


class CountryRepository(SqlAlchemyRepository):
    def __init__(self, session: AsyncSession):
        super().__init__(session)
        self.model = Country


country_repository = CountryRepository(db_manager.get_session)
