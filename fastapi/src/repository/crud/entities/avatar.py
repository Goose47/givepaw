from sqlalchemy.ext.asyncio import AsyncSession

from src.database.models import Avatar
from src.database.session_manager import db_manager
from src.repository.crud.base_crud_repository import SqlAlchemyRepository


class AvatarRepository(SqlAlchemyRepository):
    def __init__(self, session: AsyncSession):
        super().__init__(session)
        self.model = Avatar


avatar_repository = AvatarRepository(db_manager.get_session)
