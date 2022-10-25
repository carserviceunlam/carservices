from django.contrib import admin
from django.contrib.auth.models import Permission
from CarService.apps.admin_website.models.bank_accounts import BankAccounts
from CarService.apps.admin_website.models.person import Person
from CarService.apps.admin_website.models.cities import Cities
from CarService.apps.admin_website.models.provinces import Provinces
from CarService.apps.admin_website.models.employee import Employee
from CarService.apps.admin_website.models.providers import Providers
from CarService.apps.admin_website.models.companies import Companies
from CarService.apps.admin_website.models.customer import Customer
from CarService.apps.admin_website.models.vehicles import Vehicles
from CarService.apps.admin_website.models.vehicle_owner import VehicleOwner
from CarService.apps.admin_website.models.budgets import Budget
from CarService.apps.admin_website.models.repair import Repair

# Register your models here.
admin.site.register(Person)
admin.site.register(BankAccounts)
admin.site.register(Employee)
admin.site.register(Providers)
admin.site.register(Companies)
admin.site.register(Customer)
admin.site.register(Vehicles)
admin.site.register(VehicleOwner)
admin.site.register(Budget)
admin.site.register(Repair)
admin.site.register(Permission)


@admin.register(Cities)
class CitiesAdmin(admin.ModelAdmin):
    """Cities admin."""

    list_display = ("name",)


@admin.register(Provinces)
class ProvincesAdmin(admin.ModelAdmin):
    """Cities admin."""

    list_display = ("name",)
