from CarService.apps.admin_website.views import index_view


class Admin_websiteRouter:
    route_app_labels = {"admin_website"}
    # database_name = customers_views.CustomerView.username

    def db_for_read(self, model, **hints):
        if model._meta.app_label in self.route_app_labels:
            print(index_view.IndexView.database)
            return index_view.IndexView.database
        return None

    def db_for_write(self, model, **hints):
        if model._meta.app_label in self.route_app_labels:
            return index_view.IndexView.database
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        if app_label in self.route_app_labels:
            return db == index_view.IndexView.database
        return None