from django.db import models

# Create your models here


class BankAccounts(models.Model):
    """
    BankAccounts class representation.
    """

    cbu = models.CharField(max_length=255)
    bank = models.CharField(max_length=128)

    def __str__(self):
        return f"Bank: {self.bank}| CBU: {self.cbu}"

    class Meta:
        app_label = "admin_website"
