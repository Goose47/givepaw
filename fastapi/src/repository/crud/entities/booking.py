from sqlalchemy.ext.asyncio import AsyncSession

from src.database.models import Booking
from src.database.session_manager import db_manager
from src.repository.crud.base_crud_repository import SqlAlchemyRepository


class BookingRepository(SqlAlchemyRepository):
    def __init__(self, session: AsyncSession):
        super().__init__(session)
        self.model = Booking


booking_repository = BookingRepository(db_manager.get_session)
