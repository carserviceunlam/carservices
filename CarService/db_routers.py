from CarService.apps.admin_website.views import employee_views


class Admin_websiteRouter:
    route_app_labels = {"admin_website"}
    # database_name = customers_views.CustomerView.username

    def db_for_read(self, model, **hints):
        if model._meta.app_label in self.route_app_labels:
            return employee_views.EmployeePage.username
        return None

    def db_for_write(self, model, **hints):
        if model._meta.app_label in self.route_app_labels:
            return employee_views.EmployeePage.username
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        if app_label in self.route_app_labels:
            return db == employee_views.EmployeePage.username
        return None