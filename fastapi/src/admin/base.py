from sqladmin import Admin

from src.admin.characteristics.ad_status import AdStatusView
from src.admin.entities.advertisment import AdvertisementView


def setup_admin(app, engine):
    admin = Admin(app, engine, title="Otiva Billboard")
    admin.add_view(AdStatusView)
    admin.add_view(AdvertisementView)
    return admin


"""
admin.add_view(advertisement_dropdown)
admin.add_view(booking_dropdown)
admin.add_view(user_dropdown)
admin.add_view(location_dropdown)
"""
