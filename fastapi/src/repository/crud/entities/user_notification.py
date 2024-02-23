from sqlalchemy.ext.asyncio import AsyncSession

from src.database.models import UserNotification
from src.database.session_manager import db_manager
from src.repository.crud.base_crud_repository import SqlAlchemyRepository


class UserNotificationRepository(SqlAlchemyRepository):
    def __init__(self, session: AsyncSession):
        super().__init__(session)
        self.model = UserNotification


user_notification_repository = UserNotificationRepository(db_manager.get_session)
