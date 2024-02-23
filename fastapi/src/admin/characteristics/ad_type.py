from sqladmin import ModelView

from src.database.models import AdType


class AdTypeView(ModelView):
    label = "Advertisement Types"
    name = "Advertisement Type"
    name_plural = "Advertisement Types"

    column_list = [AdType.id, AdType.title]
    column_searchable_list = [AdType.id, AdType.title]
    column_sortable_list = [AdType.id, AdType.title]

    category = "Advertisement"

    page_size = 10

    icon = "fa-solid fa-chart-simple"
