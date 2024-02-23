from sqlalchemy.ext.asyncio import AsyncSession

from src.database.models import AdvertisementCategory
from src.database.session_manager import db_manager
from src.repository.crud.base_crud_repository import SqlAlchemyRepository


class AdvertisementCategoryRepository(SqlAlchemyRepository):
    def __init__(self, session: AsyncSession):
        super().__init__(session)
        self.model = AdvertisementCategory


advertisement_category_repository = AdvertisementCategoryRepository(db_manager.get_session)
