from django import forms
from vmSystem.apps.admin_website.models.vehicles import Vehicles
from vmSystem.apps.admin_website.models.customer import Customer
from vmSystem.apps.admin_website.models.companies import Companies
from vmSystem.apps.admin_website.models.vehicle_owner import VehicleOwner


class VehicleForm(forms.Form):
    """vehicle form"""

    plate_number = forms.CharField(max_length=10)
    brand = forms.CharField(max_length=64)
    model = forms.CharField(max_length=128)
    color = forms.CharField(max_length=64)
    color_code = forms.CharField(max_length=64)
    fuel = forms.CharField(max_length=32)
    kilometers = forms.IntegerField()
    state = forms.CharField(max_length=128)
    detail = forms.CharField(max_length=128)
    company = forms.ModelChoiceField(queryset=Companies.objects.all(), empty_label=None)
    customer = forms.ModelChoiceField(queryset=Customer.objects.all(), empty_label=None)

    def save(self):
        """create vehicle and create the fucking owner"""
        data = {
            "plate_number": self.cleaned_data["plate_number"],
            "brand": self.cleaned_data["brand"],
            "model": self.cleaned_data["model"],
            "color": self.cleaned_data["color"],
            "color_code": self.cleaned_data["color_code"],
            "fuel": self.cleaned_data["fuel"],
            "kilometers": self.cleaned_data["kilometers"],
            "state": self.cleaned_data["state"],
            "detail": self.cleaned_data["detail"],
            "company": self.cleaned_data["company"]
        }
        vehicle = Vehicles(**data)
        vehicle.save()
        vehicle_owner = VehicleOwner(
            customer=self.cleaned_data['customer'],
            vehicle=vehicle
        )
        vehicle_owner.save()

    def update(self, _id):
        vehicle = Vehicles.objects.get(pk=_id)
        vehicle.update_attributes(data=self.cleaned_data)
        vehicle.save()
