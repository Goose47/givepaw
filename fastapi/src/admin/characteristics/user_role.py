from sqladmin import ModelView

from src.database.models import UserRole


class UserRoleView(ModelView):
    fields = [UserRole.id, UserRole.title]

    page_size = 10

    def __init__(self):
        super().__init__(model=UserRole)

        self.label = "User Roles"
        self.name = "User Role"
        self.name_plural = "User Roles"

        self.icon = "fa fa-th-list"

        self.searchable_fields = [UserRole.id, UserRole.title]
        self.sortable_fields = [UserRole.id, UserRole.title]
