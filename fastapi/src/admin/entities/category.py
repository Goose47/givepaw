from sqladmin import ModelView

class CategoryView(ModelView):
    fields = [Category.id, Category.title, Category.order, Category.meta_title, Category.meta_description,
              Category.url, Category.parent, Category.bookable, Category.map_addressable]

    page_size = 10

    def __init__(self):
        super().__init__(model=Category)

        self.label = "Categories"
        self.name = "Category"
        self.name_plural = "Categories"

        self.icon = "fa fa-th-list"

        self.searchable_fields = [Category.id, Category.title, Category.meta_title, Category.meta_description,
                                  Category.url, Category.parent]

        self.sortable_fields = [Category.id, Category.title, Category.order, Category.meta_title,
                                Category.meta_description,
                                Category.url, Category.parent, Category.bookable, Category.map_addressable]
