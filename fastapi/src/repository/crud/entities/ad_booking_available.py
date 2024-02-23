from sqlalchemy.ext.asyncio import AsyncSession

from src.database.models import AdBookingAvailable
from src.database.session_manager import db_manager
from src.repository.crud.base_crud_repository import SqlAlchemyRepository


class AdBookingAvailableRepository(SqlAlchemyRepository):
    def __init__(self, session: AsyncSession):
        super().__init__(session)
        self.model = AdBookingAvailable


ad_booking_available_repository = AdBookingAvailableRepository(db_manager.get_session)
