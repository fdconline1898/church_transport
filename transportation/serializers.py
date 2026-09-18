from rest_framework import serializers
from .models import Rider, Driver, Trip, TripRider

class RiderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rider
        fields = '__all__'

class DriverSerializer(serializers.ModelSerializer):
    class Meta:
        model = Driver
        fields = '__all__'

class TripRiderSerializer(serializers.ModelSerializer):
    class Meta:
        model = TripRider
        fields = '__all__'

class TripSerializer(serializers.ModelSerializer):
    trip_riders = TripRiderSerializer(many=True, read_only=True)

    class Meta:
        model = Trip
        fields = '__all__'
