from vmSystem.apps.admin_website.models import (Employee, BankAccounts)
from vmSystem.apps.admin_website.models.person import Person


class EmployeeSerializer():
    def __init__(self, data, cuil):
        self.data = data
        self.cuil = cuil

    def employee_update(self):
        existing_employee = Employee.objects.get(cuil=self.cuil)
        self._update_person(existing_employee.person.dni)
        self._update_bank(existing_employee.bank_account.cbu)
        existing_employee.cuil = self.data['cuil']
        existing_employee.save()

    def _update_person(self, dni):
        person = Person.objects.get(dni=dni)
        person.dni = self.data["dni"]
        person.name = self.data["name"]
        person.last_name = self.data["last_name"]
        person.birth_day = self.data["birth_day"]
        person.phone = self.data["phone"]
        person.mobile = self.data["mobile"]
        person.email = self.data["email"]
        person.city = self.data["city"]
        person.address = self.data["address"]
        person.address_number = self.data["address_number"]
        person.save()

    def _update_bank(self, cbu):
        bank = BankAccounts.objects.get(cbu=cbu)
        bank.cbu = self.data["cbu"]
        bank.bank = self.data["bank"]
        bank.save()
