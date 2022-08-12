from django.db import models


class Country(models.Model):
    country_name = models.CharField(max_length=255)

    def __str__(self):
        return self.country_name

    class Meta:
        verbose_name_plural = "Countries"


class Region(models.Model):
    region_name = models.CharField(max_length=255)
    country = models.ForeignKey(
        Country, verbose_name="country", on_delete=models.CASCADE
    )

    def __str__(self):
        return self.region_name

    class Meta:
        verbose_name_plural = "Regions"
