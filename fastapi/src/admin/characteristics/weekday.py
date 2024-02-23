from sqladmin import ModelView

from src.database.models import Weekday


class WeekdayView(ModelView):
    fields = [Weekday.id, Weekday.title, Weekday.short_title, Weekday.order]

    page_size = 10

    def __init__(self):
        super().__init__(model=Weekday)

        self.label = "Weekdays"
        self.name = "Weekday"
        self.name_plural = "Weekdays"

        self.icon = "fa fa-th-list"

        self.searchable_fields = [Weekday.id, Weekday.title, Weekday.short_title]
        self.sortable_fields = [Weekday.id, Weekday.title, Weekday.order]
