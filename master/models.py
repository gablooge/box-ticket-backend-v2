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


class City(models.Model):
    city_name = models.CharField(max_length=255)
    region = models.ForeignKey(Region, verbose_name="region", on_delete=models.CASCADE)

    def __str__(self):
        return self.city_name

    class Meta:
        verbose_name_plural = "Cities"


class Menu(models.Model):
    description = models.CharField(max_length=255)
    role = models.IntegerField()
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.description

    class Meta:
        verbose_name_plural = "Menus"
