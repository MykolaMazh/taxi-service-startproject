from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models

class Manufacturer(models.Model):
    name = models.CharField(max_length=150, unique=True)
    country = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Driver(AbstractUser):
    license_number = models.CharField(max_length=15, unique=True)

    class Meta:
        verbose_name = "Driver"
        verbose_name_plural = "Drivers"

    def __str__(self):
        return self.username


class Car(models.Model):
    model = models.CharField(max_length=150)
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE, related_name="cars")
    drivers = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="cars")

    def __str__(self):
        return f"{self.model} {self.manufacturer}"