from django import forms
from vmSystem.apps.admin_website.models.vehicle_owner import VehicleOwner
from vmSystem.apps.admin_website.models.budgets import Budget


class BudgetForm(forms.Form):
    """Budget form."""
    owner = forms.ModelChoiceField(queryset=VehicleOwner.objects.all(),
                                   empty_label=None)
    state = forms.CharField(max_length=64)
    detail = forms.CharField(max_length=64)
    real_cost = forms.IntegerField()
    estimated_cost = forms.IntegerField()

    def save(self):
        """save the budget"""
        data = {
            "owner": self.cleaned_data["owner"],
            "state": self.cleaned_data["state"],
            "detail": self.cleaned_data["detail"],
            "real_cost": self.cleaned_data["real_cost"],
            "estimated_cost": self.cleaned_data["estimated_cost"],
        }
        budget = Budget(**data)
        budget.save()


    #def update(self):
    #    vehicle = Vehicles.objects.get(plate_number=self.cleaned_data['plate_number'])
    #    vehicle.update_attributes(data=self.cleaned_data)
    #    vehicle.save()

