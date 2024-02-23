from src.database.models import UserRole
from src.database.seeders.generic_seeder import GenericSeeder


class PermissionsSeeder(GenericSeeder):
    def __init__(self):
        super().__init__()
        self.initial_data = {
            UserRole: {
                UserRole.ADMIN: {"title": "admin"},
                UserRole.SELLER: {"title": "seller"},
                UserRole.CONSUMER: {"title": "consumer"}
            }
        }
