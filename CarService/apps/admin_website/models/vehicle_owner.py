from .customer import Customer
from .vehicles import Vehicles
from django.db import models


class VehicleOwner(models.Model):
    """
    Vehicle model class representation

    small note: to achieve the issue when an owner of the car, sell his car
    and then another owner, went to the service. we created this table
    so we can handle an history of the car, with his differents owners
    and the current owner.
    """

    customer = models.OneToOneField(Customer, on_delete=models.CASCADE)
    vehicle = models.OneToOneField(Vehicles, on_delete=models.CASCADE)
    start_date = models.DateTimeField(auto_now_add=True)
    end_date = models.DateTimeField(default=None, blank=True, null=True)

    class Meta:
        app_label = "admin_website"
