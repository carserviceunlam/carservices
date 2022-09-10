"""User forms."""

# Django
from django import forms

# Models
from vmSystem.apps.admin_website.models.employee import Employee
from vmSystem.apps.admin_website.models.person import Person
from vmSystem.apps.admin_website.models.bank_accounts import BankAccounts
from vmSystem.apps.admin_website.models.cities import Cities


class CustomDateInput(forms.DateInput):
    input_type = "date"


class EmployeeForm(forms.Form):
    """employee form."""

    def __init__(self, *args, **kwargs):
        self._context = kwargs.pop("context", None)
        self._identity_key = kwargs.pop("identity_key", None)
        super().__init__(*args, **kwargs)

    dni = forms.CharField(min_length=4, max_length=8)
    name = forms.CharField(min_length=4, max_length=64)
    last_name = forms.CharField(min_length=4, max_length=64)
    birth_day = forms.DateField(widget=CustomDateInput())
    phone = forms.IntegerField()
    mobile = forms.IntegerField()
    email = forms.CharField(min_length=6, max_length=128, widget=forms.EmailInput())
    city = forms.ModelChoiceField(queryset=Cities.objects.all(), empty_label=None)
    address = forms.CharField(min_length=4, max_length=254)
    address_number = forms.IntegerField()
    cuil = forms.CharField(min_length=4, max_length=11)
    position = forms.CharField(max_length=128)
    cbu = forms.CharField(min_length=22, max_length=255)
    bank = forms.CharField(min_length=4, max_length=128)

    def clean_dni(self):
        """
        Check by dni if exist the same element
        return: dni ok if is valid
        """

        dni = self.cleaned_data["dni"]
        dni_taken = Person.objects.filter(dni=dni).exists()
        if self._context is "update":
            if dni_taken:
                employee = Employee.objects.get(cuil=self._identity_key)
                person = Person.objects.get(dni=dni)
                if employee.person.dni == person.dni:
                    return dni
                else:
                    raise forms.ValidationError("dni is already in use")
            return dni
        if dni_taken:
            raise forms.ValidationError("dni is already in use")

        return dni

    def clean_cuil(self):
        """
        Check by cuil if exists the same employee
        """
        cuil = self.cleaned_data["cuil"]
        cuil_taken = Employee.objects.filter(cuil=cuil).exists()
        if self._context is "update":
            return cuil
        if cuil_taken:
            raise forms.ValidationError("cuil is already in use")

        return cuil

    def save(self):
        """Create employee and person"""

        # First, we create person
        data = {
            "dni": self.cleaned_data["dni"],
            "name": self.cleaned_data["name"],
            "last_name": self.cleaned_data["last_name"],
            "birth_day": self.cleaned_data["birth_day"],
            "phone": self.cleaned_data["phone"],
            "mobile": self.cleaned_data["mobile"],
            "email": self.cleaned_data["email"],
            "city": self.cleaned_data["city"],
            "address": self.cleaned_data["address"],
            "address_number": self.cleaned_data["address_number"],
        }
        person = Person(**data)
        person.save()

        # then, we create the bank account
        data = {
            "cbu": self.cleaned_data["cbu"],
            "bank": self.cleaned_data["bank"],
        }
        bank_account = BankAccounts(**data)
        bank_account.save()

        # finally, we create the employee
        employee = Employee(
            cuil=self.cleaned_data["cuil"],
            position=self.cleaned_data["position"],
            person=person,
            bank_account=bank_account,
        )
        employee.save()
