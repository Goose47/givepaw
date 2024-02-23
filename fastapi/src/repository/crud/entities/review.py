from sqlalchemy.ext.asyncio import AsyncSession

from src.database.models import Review
from src.database.session_manager import db_manager
from src.repository.crud.base_crud_repository import SqlAlchemyRepository


class ReviewRepository(SqlAlchemyRepository):
    def __init__(self, session: AsyncSession):
        super().__init__(session)
        self.model = Review


review_repository = ReviewRepository(db_manager.get_session)
