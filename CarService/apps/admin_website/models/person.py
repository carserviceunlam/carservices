from django.db import models
from .cities import Cities


class Person(models.Model):
    """Person model representation"""

    dni = models.CharField(max_length=128, default="")
    last_name = models.CharField(max_length=64)
    name = models.CharField(max_length=64)
    birth_day = models.DateTimeField()
    phone = models.IntegerField()
    mobile = models.IntegerField()
    email = models.CharField(max_length=128)
    city = models.ForeignKey(Cities, on_delete=models.PROTECT)
    address = models.CharField(max_length=254)
    address_number = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def update_attributes(self, data):
        self.dni = data["dni"]
        self.name = data["name"]
        self.last_name = data["last_name"]
        self.birth_day = data["birth_day"]
        self.phone = data["phone"]
        self.mobile = data["mobile"]
        self.email = data["email"]
        self.city = Cities.objects.get(pk=data["city"])
        self.address = data["address"]
        self.address_number = data["address_number"]

    class Meta:
        app_label = "admin_website"
