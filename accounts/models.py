from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    email = models.EmailField(max_length=254, unique=True)
    created_by = models.ForeignKey(
        "User",
        verbose_name="created by",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="createdBy",
    )
    edited_by = models.ForeignKey(
        "User",
        verbose_name="edited by",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )
    role_id = models.IntegerField(verbose_name="role", null=True)
    city_id = models.IntegerField(null=True, blank=True, verbose_name="city id")
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username", "first_name", "last_name", "role_id"]

    def __str__(self):
        return self.email


class Guest(models.Model):
    user = models.ForeignKey(User, verbose_name="user", on_delete=models.CASCADE)
    mobile = models.CharField(max_length=50, verbose_name="mobile")
    date_of_birth = models.DateField(verbose_name="date of birth")


class EventOrganizer(models.Model):
    user = models.ForeignKey(User, verbose_name="user", on_delete=models.CASCADE)
    company_name = models.CharField(max_length=255, verbose_name="company name")
    contact_no = models.CharField(max_length=50, verbose_name="contact no")
    cr_file = models.TextField(verbose_name="cr file")
    mobile = models.CharField(max_length=50, verbose_name="mobile")
