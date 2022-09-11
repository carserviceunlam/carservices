from django import forms
from CarService.apps.admin_website.models.budgets import Budget
from CarService.apps.admin_website.models.repair import Repair

class CustomDateInput(forms.DateInput):
    input_type = 'date'


class RepairForm(forms.Form):
    """Repair form."""
    budget = forms.ModelChoiceField(queryset=Budget.objects.all(),
                                    empty_label="Elegi")
    state = forms.CharField(max_length=64)
    authorize_repair = forms.BooleanField()
    entrance_detail = forms.CharField(max_length=254)

    def save(self):
        """save the repair."""
        data = {
            "budget": self.cleaned_data["budget"],
            "state": self.cleaned_data["state"],
            "authorize_repair": self.cleaned_data["authorize_repair"],
            "entrance_detail": self.cleaned_data["entrance_detail"],
        }
        repair = Repair(**data)
        repair.save()


class RepairUpdateForm(forms.Form):
    """Repair form."""
    budget = forms.ModelChoiceField(queryset=Budget.objects.all(),
                                    empty_label="Elegi")
    state = forms.CharField(max_length=64)
    authorize_repair = forms.BooleanField(required=False)
    authorize_exit = forms.BooleanField(required=False)
    entrance_detail = forms.CharField(max_length=254)
    exit_date = forms.DateField(widget=CustomDateInput())
    state = forms.CharField()
    invoice = forms.CharField()

    def save(self):
        """save the repair."""
        data = {
            "budget": self.cleaned_data["budget"],
            "state": self.cleaned_data["state"],
            "authorize_repair": self.cleaned_data["authorize_repair"],
            "entrance_detail": self.cleaned_data["entrance_detail"],
        }
        repair = Repair(**data)
        repair.save()
