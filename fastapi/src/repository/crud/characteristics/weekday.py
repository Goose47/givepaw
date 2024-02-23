from sqlalchemy.ext.asyncio import AsyncSession

from src.database.models import Weekday
from src.database.session_manager import db_manager
from src.repository.crud.base_crud_repository import SqlAlchemyRepository


class WeekdayRepository(SqlAlchemyRepository):
    def __init__(self, session: AsyncSession):
        super().__init__(session)
        self.model = Weekday


weekday_repository = WeekdayRepository(db_manager.get_session)
