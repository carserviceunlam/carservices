# Django
from django.db import models

# Models
from .bank_accounts import BankAccounts
from .cities import Cities


class Companies(models.Model):
    """
    Companies model representation.
    """

    city = models.ForeignKey(Cities, on_delete=models.CASCADE)
    bank_account = models.OneToOneField(BankAccounts, on_delete=models.CASCADE)
    cuit = models.CharField(max_length=11)
    business_name = models.CharField(max_length=128)
    contact_person = models.CharField(max_length=128, blank=True)
    phone = models.CharField(max_length=20, blank=True)
    mobile = models.CharField(max_length=20, blank=True)
    address = models.CharField(max_length=254)
    address_number = models.IntegerField()
    email = models.CharField(max_length=200, blank=True)
    website = models.URLField(max_length=200, blank=True)
    details = models.TextField(blank=True)
    company_type = models.CharField(max_length=64)
    state = models.CharField(max_length=64)

    def __str__(self):
        return f"Aseguradora: {self.business_name}"

    class Meta:
        app_label = 'admin_website'
