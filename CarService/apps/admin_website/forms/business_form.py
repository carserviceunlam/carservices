from django import forms
from CarService.apps.admin_website.models.customer import Customer
from CarService.apps.admin_website.models.bank_accounts import BankAccounts


class BusinessForm(forms.Form):
    """Business Form."""
    cuit = forms.CharField(min_length=11, max_length=11)
    business_name = forms.CharField(min_length=2, max_length=128)
    cbu = forms.CharField(min_length=22, max_length=255)
    bank = forms.CharField(min_length=4, max_length=128)

    def save(self):
        """create business account"""
        data = {
            "cuit": self.cleaned_data["cuit"],
            "business_name": self.cleaned_data["business_name"],
            "last_name": "last_name",
        }
        customer = Customer(**data)
        customer.save()
        data = {
            "cbu": self.cleaned_data["cbu"],
            "bank": self.cleaned_data["bank"],
        }
        bank_account = BankAccounts(**data)
        bank_account.save()




