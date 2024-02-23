from sqladmin import ModelView

from src.database.models import City


class CityView(ModelView):
    fields = [City.id, City.title]

    page_size = 10

    def __init__(self):
        super().__init__(model=City)

        self.label = "Cities"
        self.name = "City"
        self.name_plural = "Cities"

        self.icon = "fa fa-th-list"

        self.searchable_fields = [City.id, City.title]
        self.sortable_fields = [City.id, City.title]
