from django.db import models


class Provinces(models.Model):
    """
    Provinces model representation.
    """

    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name

    class Meta:
        app_label = "admin_website"
