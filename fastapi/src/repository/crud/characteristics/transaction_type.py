from sqlalchemy.ext.asyncio import AsyncSession

from src.database.models import TransactionType
from src.database.session_manager import db_manager
from src.repository.crud.base_crud_repository import SqlAlchemyRepository


class TransactionTypeRepository(SqlAlchemyRepository):
    def __init__(self, session: AsyncSession):
        super().__init__(session)
        self.model = TransactionType


transaction_type_repository = TransactionTypeRepository(db_manager.get_session)
