from sqladmin import ModelView

from src.database.models import Advertisement


class AdvertisementView(ModelView, model=Advertisement):
    label = "Advertisements"
    name = "Advertisement"
    name_plural = "Advertisements"

    column_list = [Advertisement.id, Advertisement.title, Advertisement.user_description,
                   Advertisement.user, Advertisement.ad_status, Advertisement.ad_type, Advertisement.price,
                   Advertisement.categories,
                   Advertisement.created_at, Advertisement.updated_at, Advertisement.deleted_at]

    column_searchable_list = [Advertisement.id, Advertisement.title, Advertisement.user_description]

    column_sortable_list = [Advertisement.id, Advertisement.title, Advertisement.user_description,
                            Advertisement.price,
                            Advertisement.created_at, Advertisement.updated_at, Advertisement.deleted_at]

    page_size = 10

    icon = "fa fa-th-list"

    category = "Advertisement"
