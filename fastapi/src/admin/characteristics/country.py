from sqladmin import ModelView

from src.database.models import Country


class CountryView(ModelView):
    fields = [Country.id, Country.title]

    page_size = 10

    def __init__(self):
        super().__init__(model=Country)

        self.label = "Countries"
        self.name = "Country"
        self.name_plural = "Countries"

        self.icon = "fa fa-th-list"

        self.searchable_fields = [Country.id, Country.title]
        self.sortable_fields = [Country.id, Country.title]
