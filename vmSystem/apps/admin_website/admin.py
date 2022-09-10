from django.contrib import admin
from vmSystem.apps.admin_website.models.bank_accounts import BankAccounts
from vmSystem.apps.admin_website.models.person import Person
from vmSystem.apps.admin_website.models.cities import Cities
from vmSystem.apps.admin_website.models.provinces import Provinces
from vmSystem.apps.admin_website.models.employee import Employee
from vmSystem.apps.admin_website.models.providers import Providers
from vmSystem.apps.admin_website.models.companies import Companies
from vmSystem.apps.admin_website.models.customer import Customer
from vmSystem.apps.admin_website.models.vehicles import Vehicles
from vmSystem.apps.admin_website.models.vehicle_owner import VehicleOwner
from vmSystem.apps.admin_website.models.budgets import Budget
from vmSystem.apps.admin_website.models.repair import Repair
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


@admin.register(Cities)
class CitiesAdmin(admin.ModelAdmin):
    """Cities admin."""

    list_display = ('name',)


@admin.register(Provinces)
class ProvincesAdmin(admin.ModelAdmin):
    """Cities admin."""

    list_display = ('name',)
