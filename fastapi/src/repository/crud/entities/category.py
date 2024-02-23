from sqlalchemy.ext.asyncio import AsyncSession

from src.database.models import Category
from src.database.session_manager import db_manager
from src.repository.crud.base_crud_repository import SqlAlchemyRepository


class CategoryRepository(SqlAlchemyRepository):
    def __init__(self, session: AsyncSession):
        super().__init__(session)
        self.model = Category


category_repository = CategoryRepository(db_manager.get_session)
