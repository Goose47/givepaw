from sqlalchemy.ext.asyncio import AsyncSession

from src.database.models import AdType, BookingType, FilterType, TransactionType, City, Country, Priority, Weekday
from src.database.seeders.generic_seeder import GenericSeeder


class UtilsSeeder(GenericSeeder):
    def __init__(self):
        super().__init__()
        self.initial_data = {
            # City: {},
            # Country: {},
            Priority: {},
            Weekday: {
                Weekday.MONDAY: {"title": "Monday", "order": 1, "short_title": "Mon"},
                Weekday.TUESDAY: {"title": "Tuesday", "order": 2, "short_title": "Tue"},
                Weekday.WEDNESDAY: {"title": "Wednesday", "order": 3, "short_title": "Wed"},
                Weekday.THURSDAY: {"title": "Thursday", "order": 4, "short_title": "Thu"},
                Weekday.FRIDAY: {"title": "Friday", "order": 5, "short_title": "Fri"},
                Weekday.SATURDAY: {"title": "Saturday", "order": 6, "short_title": "Sat"},
                Weekday.SUNDAY: {"title": "Sunday", "order": 7, "short_title": "Sun"}
            }
        }
