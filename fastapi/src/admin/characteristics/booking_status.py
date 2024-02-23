from sqladmin import ModelView

from src.database.models import BookingStatus


class BookingStatusView(ModelView):
    fields = [BookingStatus.id, BookingStatus.title]

    page_size = 10

    def __init__(self):
        super().__init__(model=BookingStatus)

        self.label = "Booking Statuses"
        self.name = "Booking Status"
        self.name_plural = "Booking Statuses"

        self.icon = "fa fa-th-list"

        self.searchable_fields = [BookingStatus.id, BookingStatus.title]
        self.sortable_fields = [BookingStatus.id, BookingStatus.title]
