from sqladmin import ModelView

from src.database.models import UserStatus


class UserStatusView(ModelView):
    fields = [UserStatus.id, UserStatus.title, UserStatus.is_available]

    page_size = 10

    def __init__(self):
        super().__init__(model=UserStatus)

        self.label = "User Statuses"
        self.name = "User Status"
        self.name_plural = "User Statuses"

        self.icon = "fa fa-th-list"

        self.searchable_fields = [UserStatus.id, UserStatus.title, UserStatus.is_available]
        self.sortable_fields = [UserStatus.id, UserStatus.title, UserStatus.is_available]

