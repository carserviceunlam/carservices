from django.db import models
from .companies import Companies


class Vehicles(models.Model):
    """
    Vehicles model class reprensentation.
    """

    plate_number = models.CharField(max_length=10, default="N/A")
    company = models.OneToOneField(Companies, on_delete=models.CASCADE)
    brand = models.CharField(max_length=128)
    model = models.CharField(max_length=128)
    color = models.CharField(max_length=64)
    color_code = models.CharField(max_length=64)
    fuel = models.CharField(max_length=32)
    kilometers = models.IntegerField()
    detail = models.CharField(max_length=254)
    state = models.CharField(max_length=64)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def update_attributes(self, data):
        self.plate_number = data["plate_number"]
        self.company = data["company"]
        self.brand = data["brand"]
        self.model = data["model"]
        self.color = data["color"]
        self.color_code = data["color_code"]
        self.fuel = data["fuel"]
        self.kilometers = data["kilometers"]
        self.detail = data["detail"]
        self.state = data["state"]

    class Meta:
        app_label = "admin_website"
