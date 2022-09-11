from django.db import models
from CarService.apps.admin_website.models.budgets import Budget


class Repair(models.Model):
    """Repair model representation."""
    budget = models.OneToOneField(Budget, on_delete=models.CASCADE)
    income_date = models.DateTimeField(auto_now_add=True)
    exit_date = models.DateTimeField(default=None, blank=True, null=True)
    state = models.CharField(max_length=64, default=None, blank=True, null=True)
    invoice = models.IntegerField(default=None, blank=True, null=True)
    authorize_repair = models.BooleanField(default=None, blank=True, null=True)
    authorize_exit = models.BooleanField(default=None, blank=True, null=True)
    entrance_detail = models.CharField(max_length=254,
                                       default=None,
                                       blank=True,
                                       null=True)
    exit_detail = models.CharField(max_length=254, default=None, blank=True, null=True)
