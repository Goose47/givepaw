from sqladmin import ModelView

from src.database.models import BookingType


class BookingTypeView(ModelView):
    fields = [BookingType.id, BookingType.title]

    page_size = 10

    def __init__(self):
        super().__init__(model=BookingType)

        self.label = "Booking Types"
        self.name = "Booking Type"
        self.name_plural = "Booking Types"

        self.icon = "fa fa-th-list"

        self.searchable_fields = [BookingType.id, BookingType.title]
        self.sortable_fields = [BookingType.id, BookingType.title]
