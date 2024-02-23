from sqlalchemy.ext.asyncio import AsyncSession

from src.database.models import Advertisement
from src.database.session_manager import db_manager
from src.repository.crud.base_crud_repository import SqlAlchemyRepository


class AdvertisementRepository(SqlAlchemyRepository):
    def __init__(self, session: AsyncSession):
        super().__init__(session)
        self.model = Advertisement


advertisement_repository = AdvertisementRepository(db_manager.get_session)
