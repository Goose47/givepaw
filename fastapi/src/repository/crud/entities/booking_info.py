from sqlalchemy.ext.asyncio import AsyncSession

from src.database.models import BookingInfo
from src.database.session_manager import db_manager
from src.repository.crud.base_crud_repository import SqlAlchemyRepository


class BookingInfoRepository(SqlAlchemyRepository):
    def __init__(self, session: AsyncSession):
        super().__init__(session)
        self.model = BookingInfo


booking_info_repository = BookingInfoRepository(db_manager.get_session)
