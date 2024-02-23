from sqlalchemy.ext.asyncio import AsyncSession

from src.database.models import BookingType
from src.database.session_manager import db_manager
from src.repository.crud.base_crud_repository import SqlAlchemyRepository


class BookingTypeRepository(SqlAlchemyRepository):
    def __init__(self, session: AsyncSession):
        super().__init__(session)
        self.model = BookingType


booking_type_repository = BookingTypeRepository(db_manager.get_session)
