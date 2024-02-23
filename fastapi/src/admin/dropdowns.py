"""
from src.admin.characteristics.ad_type import AdTypeView
from src.admin.characteristics.ad_status import AdStatusView
from src.admin.characteristics.booking_status import BookingStatusView
from src.admin.characteristics.booking_type import BookingTypeView
from src.admin.characteristics.city import CityView
from src.admin.characteristics.country import CountryView
from src.admin.characteristics.user_role import UserRoleView
from src.admin.characteristics.user_status import UserStatusView
from src.admin.characteristics.weekday import WeekdayView
from src.admin.entities.advertisment import AdvertisementView
from src.admin.entities.category import CategoryView
from src.admin.entities.user import UserView

advertisement_dropdown = DropDown(
    "Advertisements Settings",
    icon="fa fa-table",
    views=[
        AdStatusView,
        AdTypeView,
        AdvertisementView,
        CategoryView
    ],
    always_open=False
)

booking_dropdown = DropDown(
    "Booking Settings",
    icon="fa fa-table",
    views=[
        BookingTypeView,
        BookingStatusView
    ],
    always_open=False
)

user_dropdown = DropDown(
    "Users",
    icon="fa fa-table",
    views=[UserStatusView,
           UserRoleView,
           UserView
           ],
    always_open=False
)

location_dropdown = DropDown(
    "Location Settings",
    icon="fa fa-table",
    views=[CountryView,
           CityView,
           WeekdayView
           ],
    always_open=False
)
"""
