from src.schemas import BaseResponseSchema

from src.schemas.entities.base import BaseEntityTime


class UserNotification(BaseEntityTime):
    title: str
    description: str

    notification_type: str  # "models/entities/category/booking"
    notification_content: int

    user_id: int


class UserNotificationResponse(UserNotification, BaseResponseSchema):
    pass


class UserNotificationCreate(UserNotification):
    pass


class UserNotificationUpdate(UserNotification):
    pass
