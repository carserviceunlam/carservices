from django.db import models
from .vehicle_owner import VehicleOwner


class Budget(models.Model):
    """budget model representation."""
    owner = models.ForeignKey(VehicleOwner, on_delete=models.CASCADE)
    budget_date = models.DateTimeField(auto_now=True)
    state = models.CharField(max_length=64, default='')
    detail = models.CharField(max_length=64, default='')
    real_cost = models.IntegerField()
    estimated_cost = models.IntegerField()
