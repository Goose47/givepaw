from sqlalchemy.ext.asyncio import AsyncSession

from src.database.models import AdType, BookingType, FilterType, TransactionType
from src.database.seeders.generic_seeder import GenericSeeder


class TypesSeeder(GenericSeeder):
    def __init__(self):
        super().__init__()
        self.initial_data = {
            AdType: {
                AdType.TYPE_1: {"title": "type1"},
                AdType.TYPE_2: {"title": "type2"},
                AdType.TYPE_3: {"title": "type3"},
            },
            BookingType: {
                BookingType.TYPE_1: {"title": "type1"},
                BookingType.TYPE_2: {"title": "type2"},
                BookingType.TYPE_3: {"title": "type3"},
            },
            FilterType: {
                FilterType.TYPE_1: {"title": "type1", "functional_title": "type1"},
                FilterType.TYPE_2: {"title": "type2", "functional_title": "type2"},
                FilterType.TYPE_3: {"title": "type3", "functional_title": "type3"},
            },
            TransactionType: {
                TransactionType.TYPE_1: {"title": "type1"},
                TransactionType.TYPE_2: {"title": "type2"},
                TransactionType.TYPE_3: {"title": "type3"},
            }
        }
