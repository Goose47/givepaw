from sqlalchemy.ext.asyncio import AsyncSession

from src.database.models import Address
from src.database.session_manager import db_manager
from src.repository.crud.base_crud_repository import SqlAlchemyRepository


class AddressRepository(SqlAlchemyRepository):
    def __init__(self, session: AsyncSession):
        super().__init__(session)
        self.model = Address


address_repository = AddressRepository(db_manager.get_session)
