from django.db import models
from .cities import Cities
from .person import Person


class Customer(models.Model):
    """customer model representation"""

    business_name = models.CharField(max_length=128)
    cuit = models.CharField(max_length=255, default='')
    status = models.BooleanField(default='True')
    last_name = models.CharField(max_length=64)
    person = models.ForeignKey(Person,
                               default=None,
                               blank=True,
                               null=True,
                               on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def update_atrributes(self, data):
        """update atritbues of the model."""
        self.business_name = data["business_name"]
        self.cuit = data["cuit"]
        self.last_name = "last_name"
        self.person.dni = data["dni"]
        self.person.name = data["name"]
        self.person.last_name = data["last_name"]
        self.person.birth_day = data["birth_day"]
        self.person.phone = data["phone"]
        self.person.mobile = data["mobile"]
        self.person.email = data["email"]
        self.person.city = Cities.objects.get(pk=data["city"])
        self.person.address = data["address"]
        self.person.address_number = data["address_number"]

    def __str__(self):
        return self.business_name

    class Meta:
        app_label = "admin_website"
