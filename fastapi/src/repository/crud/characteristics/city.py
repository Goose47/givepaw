from sqlalchemy.ext.asyncio import AsyncSession

from src.database.models import City
from src.database.session_manager import db_manager
from src.repository.crud.base_crud_repository import SqlAlchemyRepository


class CityRepository(SqlAlchemyRepository):
    def __init__(self, session: AsyncSession):
        super().__init__(session)
        self.model = City


city_repository = CityRepository(db_manager.get_session)
