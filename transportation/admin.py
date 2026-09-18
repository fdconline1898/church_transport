from django.contrib import admin
from .models import Rider, Driver, Trip, TripRider

admin.site.register(Rider)
admin.site.register(Driver)
admin.site.register(Trip)
admin.site.register(TripRider)
