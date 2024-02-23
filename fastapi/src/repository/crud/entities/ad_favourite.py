from sqlalchemy.ext.asyncio import AsyncSession

from src.database.models import AdFavourite
from src.database.session_manager import db_manager
from src.repository.crud.base_crud_repository import SqlAlchemyRepository


class AdFavouriteRepository(SqlAlchemyRepository):
    def __init__(self, session: AsyncSession):
        super().__init__(session)
        self.model = AdFavourite


ad_favourite_repository = AdFavouriteRepository(db_manager.get_session)
