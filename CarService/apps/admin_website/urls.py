# Django
from django.urls import path

# Views

from CarService.apps.admin_website.views.vehicle_views import (
    VehicleView,
    VehicleDelete,
    VehicleCreateView,
    VehicleDetailView,
)

from CarService.apps.admin_website.views.customers_views import (
    CustomerView,
    CustomerDetailView,
    CustomerDelete,
    CustomerCreate,
    CustomerCreateBusiness,
    CustomerUpdateBusinessView,
)
from CarService.apps.admin_website.views.employee_views import (
    EmployeeCreate,
    EmployeeDelete,
    EmployeeDetailView,
    EmployeePage,
)
from CarService.apps.admin_website.views.company_views import (
    ListCompaniesView,
    EditCompanyView,
    CreateCompanyView,
    CompanyDelete
)
from CarService.apps.admin_website.views.budget_view import (
    BudgetList,
    BudgetCreateView,
    BudgetDeleteView,
    BudgetDetailView,
)
from CarService.apps.admin_website.views.repair_views import (
    RepairList,
    RepairDeleteView,
    RepairUpdateView,
    RepairCreateView,
)
from CarService.apps.admin_website.views.provider_views import ListProvidersView


urlpatterns = [
    path('companies', ListCompaniesView.as_view(), name='companies_list'),
    path('company/<int:id>/edit', EditCompanyView.as_view(), name='company_edit'),
    path("company/create", CreateCompanyView.as_view(), name="company_create"),
    path("company/<pk>/delete", CompanyDelete.as_view(), name="company_delete"),
    path("", EmployeePage.as_view(), name="employees_list"),
    path("employees/create/", EmployeeCreate.as_view(), name="employees_create"),
    path("employees/<pk>/delete/", EmployeeDelete.as_view(), name="employees_delete"),
    path(
        "employees/<str:cuil>/",
        EmployeeDetailView.as_view(),
        name="employees_detail",
    ),
    path("customers/", CustomerView.as_view(), name="customer_list"),
    path("customers/create/", CustomerCreate.as_view(), name="customer_create"),
    path("customers/create/business",
         CustomerCreateBusiness.as_view(),
         name="customer_create_business"),

    path("customers/<pk>/update/",
         CustomerUpdateBusinessView.as_view(),
         name="customer_update_business"),
    path("customers/<int:id>/edit", CustomerDetailView.as_view(), name="customer_edit"),
    path("customers/<pk>/delete/", CustomerDelete.as_view(), name="customer_delete"),
    path("vehicles/", VehicleView.as_view(), name="vehicles_list"),
    path("vehicles/create/", VehicleCreateView.as_view(), name="vehicles"
                                                               "_create"),
    path("vehicles/<int:id>/edit/", VehicleDetailView.as_view(),
         name="vehicle_edit"),
    path("vehicles/<pk>/delete/", VehicleDelete.as_view(), name="vehicles_delete"),
    path("providers", ListProvidersView.as_view(), name="providers_list"),
    path("budget/", BudgetList.as_view(), name="budget_list"),
    path("budget/create/", BudgetCreateView.as_view(), name="budget_create"),
    path("budget/<pk>/delete/", BudgetDeleteView.as_view(), name="budget_delete"),
    path("budget/<pk>/update/", BudgetDetailView.as_view(), name="budget_update"),
    path("repairs/", RepairList.as_view(), name="repair_list"),
    path("repairs/<pk>/delete/", RepairDeleteView.as_view(), name="repair_delete"),
    path("repairs/<int:id>/update/", RepairUpdateView.as_view(), name="repair_update"),
    path("repairs/create/", RepairCreateView.as_view(), name="repair_create"),
]
