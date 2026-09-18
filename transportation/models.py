from django.db import models
from django.contrib.auth.models import User

class Rider(models.Model):
    full_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    email = models.EmailField(blank=True, null=True)
    address_line1 = models.CharField(max_length=200)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=50)
    zip_code = models.CharField(max_length=10)
    emergency_contact_name = models.CharField(max_length=100, blank=True, null=True)
    emergency_contact_phone = models.CharField(max_length=20, blank=True, null=True)
    mobility_needs = models.TextField(blank=True, null=True)
    preferred_service_time = models.CharField(max_length=50)
    recurring_weekly = models.BooleanField(default=True)
    notes = models.TextField(blank=True, null=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.full_name


class Driver(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    full_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    vehicle_description = models.CharField(max_length=200, blank=True, null=True)
    vehicle_capacity = models.PositiveIntegerField(default=4)
    license_number = models.CharField(max_length=50, blank=True, null=True)
    insurance_info = models.TextField(blank=True, null=True)
    weekly_availability = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.full_name


class Trip(models.Model):
    STATUS_CHOICES = [
        ('scheduled', 'Scheduled'),
        ('confirmed', 'Confirmed'),
        ('in_progress', 'In Progress'),
        ('completed', 'Completed'),
        ('cancelled', 'Cancelled'),
    ]

    date = models.DateField()
    service_time = models.CharField(max_length=50)
    driver = models.ForeignKey(Driver, on_delete=models.SET_NULL, null=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='scheduled')
    notes = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.date} - {self.service_time}"


class TripRider(models.Model):
    trip = models.ForeignKey(Trip, on_delete=models.CASCADE, related_name='trip_riders')
    rider = models.ForeignKey(Rider, on_delete=models.CASCADE)
    pickup_time = models.TimeField(blank=True, null=True)
    dropoff_time = models.TimeField(blank=True, null=True)
    pickup_status = models.CharField(max_length=20, default='pending')
    dropoff_status = models.CharField(max_length=20, default='pending')
    special_instructions = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.trip} - {self.rider}"
