from sqladmin import ModelView

from src.database.models import AdStatus


class AdStatusView(ModelView, model=AdStatus):
    label = "Advertisement Statuses"
    name = "Advertisement Status"
    name_plural = "Advertisement Statuses"

    column_list = [AdStatus.id, AdStatus.title, AdStatus.is_shown]
    column_searchable_list = [AdStatus.id, AdStatus.title, AdStatus.is_shown]
    column_sortable_list = [AdStatus.id, AdStatus.title, AdStatus.is_shown]

    category = "Advertisement"

    page_size = 10

    icon = "fa-solid fa-chart-simple"
