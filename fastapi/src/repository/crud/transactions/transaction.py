from sqlalchemy.ext.asyncio import AsyncSession

from src.database.models import Transaction
from src.database.session_manager import db_manager
from src.repository.crud.base_crud_repository import SqlAlchemyRepository


class TransactionRepository(SqlAlchemyRepository):
    def __init__(self, session: AsyncSession):
        super().__init__(session)
        self.model = Transaction


transaction_repository = TransactionRepository(db_manager.get_session)
