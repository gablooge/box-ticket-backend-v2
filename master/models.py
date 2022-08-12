from django.db import models


class Country(models.Model):
    country_name = models.CharField(max_length=255)

    def __str__(self):
        return self.country_name
