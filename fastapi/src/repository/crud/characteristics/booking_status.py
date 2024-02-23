from sqlalchemy.ext.asyncio import AsyncSession

from src.database.models import BookingStatus
from src.database.session_manager import db_manager
from src.repository.crud.base_crud_repository import SqlAlchemyRepository


class BookingStatusRepository(SqlAlchemyRepository):
    def __init__(self, session: AsyncSession):
        super().__init__(session)
        self.model = BookingStatus


booking_status_repository = BookingStatusRepository(db_manager.get_session)
