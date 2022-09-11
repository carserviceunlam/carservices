from django.db import models
from .person import Person
from .bank_accounts import BankAccounts


class Employee(models.Model):
    """
    Employee class representation.
    """

    cuil = models.CharField(max_length=255)
    position = models.CharField(max_length=128)
    admission_date = models.DateTimeField(auto_now_add=True)
    departure_date = models.DateTimeField(null=True, blank=True)
    person = models.OneToOneField(Person, on_delete=models.CASCADE)
    bank_account = models.ForeignKey(BankAccounts, on_delete=models.CASCADE)

    class Meta:
        app_label = "admin_website"
