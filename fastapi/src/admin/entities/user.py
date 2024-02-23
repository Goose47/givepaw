from sqladmin import ModelView

from src.database.models import User


class UserView(ModelView):
    fields = [User.id, User.first_name, User.last_name, User.email, User.phone_number, User.user_status,
              User.email_verified_at, User.phone_verified_at, User.created_at, User.updated_at,
              User.deleted_at]  # avatar

    page_size = 10

    def __init__(self):
        super().__init__(model=User)

        self.label = "Users"
        self.name = "User"
        self.name_plural = "Users"

        self.icon = "fa fa-th-list"

        self.searchable_fields = [User.id, User.first_name, User.last_name, User.email, User.phone_number]
        self.sortable_fields = [User.id, User.first_name, User.last_name, User.email, User.phone_number,
                                User.user_status, User.email_verified_at, User.phone_verified_at,
                                User.created_at, User.updated_at, User.deleted_at]
