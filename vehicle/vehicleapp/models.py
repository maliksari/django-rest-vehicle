from django.db import models
from django.utils import timezone
from django.db.models.deletion import CASCADE

# Create your models here.


class VehicleModel(models.Model):
    name = models.CharField(max_length=100, blank=True)
    brand = models.CharField(max_length=100, blank=True)
    created_at = models.DateTimeField(
        auto_now_add=True)
    updated_at = models.DateTimeField(
        null=True, blank=True)
    deleted_at = models.DateTimeField(blank=True, null=True, default=None)
    is_deleted = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    def soft_delete(self):
        self.is_deleted = True
        self.deleted_at = timezone.now()
        self.save()


class Vehicle(models.Model):
    vehicle = models.ForeignKey(VehicleModel, on_delete=CASCADE)
    km = models.IntegerField()
    plate = models.CharField(max_length=100, blank=True)
    chassis_number = models.IntegerField()
    created_at = models.DateTimeField(
        auto_now_add=True)
    updated_at = models.DateTimeField(
        null=True, blank=True)
    deleted_at = models.DateTimeField(blank=True, null=True, default=None)
    is_deleted = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.plate

    def soft_delete(self):
        self.is_deleted = True
        self.deleted_at = timezone.now()
        self.save()