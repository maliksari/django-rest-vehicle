# from django.db import models
# from django.db.models import fields
from ..models import Vehicle, VehicleModel
from rest_framework import serializers


class VehicleModelSerializers(serializers.ModelSerializer):
    class Meta:
        model = VehicleModel
        fields = '__all__'


class VehicleSerializers(serializers.ModelSerializer):
    class Meta:
        model = Vehicle
        fields = '__all__'
