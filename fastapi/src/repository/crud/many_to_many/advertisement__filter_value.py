from sqlalchemy.ext.asyncio import AsyncSession
from src.database.session_manager import db_manager
from src.repository.crud.base_crud_repository import SqlAlchemyRepository
from src.schemas.many_to_many.advertisement__filter_value import AdvertisementFilterValue


class AdvertisementFilterValueRepository(SqlAlchemyRepository):
    def __init__(self, session: AsyncSession):
        super().__init__(session)
        self.model = AdvertisementFilterValue


advertisement_filter_value_repository = AdvertisementFilterValueRepository(db_manager.get_session)
