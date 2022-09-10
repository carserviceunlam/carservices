# Django
from django.db import models
from .provinces import Provinces


class Cities(models.Model):
    """
    Cities model representation.
    """

    province = models.ForeignKey(Provinces, on_delete=models.CASCADE)
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name

    class Meta:
        app_label = "admin_website"
